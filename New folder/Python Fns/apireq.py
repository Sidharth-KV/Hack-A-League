from transformers import pipeline
from img2txt import img2str


#def summarize():

summarizer = pipeline("summarization",model = "facebook/bart-large-cnn")
print("summarization")
user_input = "Python is a high-level, interpreted programming language known for its simplicity and readability, making it a popular choice among beginners and experienced developers alike. It was created by Guido van Rossum and released in 1991. Python's syntax allows developers to express concepts in fewer lines of code compared to languages like C++ or Java. Its versatility allows it to be used in a wide range of applications. In web development, frameworks like Django and Flask make it easy to build robust websites and applications. In data science, Python’s libraries like Pandas, NumPy, and Matplotlib provide tools for data manipulation, analysis, and visualization. Python is also widely used in machine learning and artificial intelligence thanks to libraries like TensorFlow, Keras, and Scikit-learn. Additionally, Python is commonly used for automation, where it helps streamline repetitive tasks with simple scripts. From game development using libraries like Pygame, to networking, cybersecurity, and scientific computing, Python's vast ecosystem makes it an invaluable tool for a variety of domains."
# user_input = img2str()
input_words = user_input.split()
input_words_len = len(input_words)
print("input words length: ", input_words_len)

max = input_words_len*0.6
min = input_words_len*0.1

summary = summarizer(user_input, max_length= max, min_length= min, do_sample = False)

print(summary)
item = summary[0]
new_summary = item.get('summary_text')
split = new_summary.split()

print("Number of words in summary: ", len(split))