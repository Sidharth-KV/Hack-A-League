from summarizer import summarize

def txttotext(txt_file):
    with open(txt_file,"r") as file:
        content = file.read()
    summ_txt =  summarize(content)
    return summ_txt


