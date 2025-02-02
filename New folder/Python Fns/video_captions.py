import edge_tts
import asyncio
import pysrt
import cv2
import subprocess
from datetime import timedelta

def read_text_file(file_path):
    """Read text from a file"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().strip()
            print(f" Read {len(text)} characters from {file_path}")
            return text
    except FileNotFoundError:
        print(f" Error: File {file_path} not found!")
        return ""

def split_text_into_chunks(text, words_per_chunk=5):
    """Split text into chunks of 4-5 words"""
    words = text.split()
    if not words:
        print(" Error: No words found in the text file!")
        return []
    
    chunks = [" ".join(words[i:i+words_per_chunk]) for i in range(0, len(words), words_per_chunk)]
    print(f" Split text into {len(chunks)} chunks")
    return chunks

def get_video_duration(video_path):
    """Get video duration in seconds"""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f" Error: Unable to open video file {video_path}")
        return 0

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    if fps > 0:
        duration = frame_count / fps
        print(f" Video duration: {duration:.2f} seconds")
        return duration
    else:
        print(" Error: FPS is 0, video file might be corrupted!")
        return 0

def create_srt_file(text_chunks, video_duration, srt_filename="subtitles.srt"):
    """Generate an SRT file ensuring last subtitle appears within 3 seconds of video end"""
    if not text_chunks:
        print(" Error: No subtitles to write!")
        return ""

    subs = pysrt.SubRipFile()
    
    total_chunks = len(text_chunks)
    subtitle_duration = 2  # Default duration per subtitle in seconds
    total_subtitle_time = total_chunks * subtitle_duration  

    # Adjust duration if subtitles exceed (video_duration - 3 sec)
    if total_subtitle_time > video_duration - 3 and total_chunks > 0:
        adjusted_duration = max((video_duration - 3) / total_chunks, 1)  # Ensure at least 1 sec per subtitle
    else:
        adjusted_duration = subtitle_duration

    print(f" Setting each subtitle duration to {adjusted_duration:.2f} seconds")

    start_time = timedelta(seconds=0)
    duration = timedelta(seconds=adjusted_duration)

    for idx, chunk in enumerate(text_chunks):
        end_time = start_time + duration  

        sub = pysrt.SubRipItem(
            index=idx + 1,
            start=pysrt.SubRipTime(start_time.seconds, start_time.microseconds // 1000),
            end=pysrt.SubRipTime(end_time.seconds, end_time.microseconds // 1000),
            text=chunk.strip()
        )

        subs.append(sub)
        start_time = end_time  

    subs.save(srt_filename, encoding="utf-8")
    print(f" SRT file saved as {srt_filename}")
    return srt_filename

def overlay_subtitles_ffmpeg(video_path, subtitle_file, output_path="output.mp4"):
    """Overlay subtitles using FFmpeg and encode in H.264"""
    if not subtitle_file:
        print(" Error: No subtitle file found. Skipping FFmpeg processing.")
        return
    
    subtitle_file = subtitle_file.replace("\\", "/")  # Ensure proper path format for FFmpeg
    video_path = video_path.replace("\\", "/")  # Ensure proper path format for FFmpeg
    output_path = output_path.replace("\\", "/")  # Ensure proper path format for FFmpeg

    # Debug: Check if the paths are correct
    print(f"Video Path: {video_path}")
    print(f"Subtitle File: {subtitle_file}")
    print(f"Output Path: {output_path}")

    # Command to overlay subtitles using FFmpeg
    command = [
        "ffmpeg",
        "-i", video_path,  # Input video
        "-vf", f"subtitles={subtitle_file}:force_style='Fontsize=24,PrimaryColour=&Hffffff&'",  # Add subtitles
        "-c:v", "libx264",  # Use H.264 codec
        "-preset", "slow",  # Better compression
        "-crf", "23",  # Adjust quality (lower = better)
        "-c:a", "aac",  # Use AAC for audio
        "-b:a", "192k",  # Audio bitrate
        "-y", output_path  # Output file
    ]

    # Print out the FFmpeg command to check it
    print(f"Running FFmpeg command: {' '.join(command)}")
    
    # Run the FFmpeg command and capture any error output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Check if the FFmpeg command was successful
    if result.returncode == 0:
        print(f"Video saved as {output_path}")
    else:
        print("FFmpeg Error:", result.stderr.decode())
