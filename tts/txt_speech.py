import edge_tts
import asyncio
import pygame
#pip install edge-tts pygame

async def text_to_speech(text, output_file, voice="en-US-JennyNeural", rate="+20%"):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    await communicate.save(output_file)

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

text = "Meow meow, my fellow friends. Drink your H2O."
output_file = "wee.mp3"

asyncio.run(text_to_speech(text, output_file))
play_audio(output_file)
