def txttotext(txt_file):
    with open(txt_file,"r") as file:
        content = file.read()
    return content

print(txttotext("sample.txt"))