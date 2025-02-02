from transformers import pipeline
from process_image import img2str
from storage import store

def summarize(user_input):
    try:
        summarizer = pipeline("summarization",model = "facebook/bart-large-cnn")
        input_words = user_input.split()
        input_words_len = len(input_words)
        print("input words length: ", input_words_len)

        max = input_words_len*0.6
        min = input_words_len*0.1

        summary = summarizer(user_input, max_length= max, min_length= min, do_sample = False)

        item = summary[0]
        new_summary = item.get('summary_text')
        split = new_summary.split()
        
        store(new_summary)

    except Exception as e:
        print("An error occurred: ", e)
        return None