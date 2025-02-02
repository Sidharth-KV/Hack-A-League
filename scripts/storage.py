import os

file_name = r"C:\Users\Lenovo\Desktop\New folder\temp\temp.txt"
def store(item):
    if os.path.exists(file_name):
        with open(file_name, "w") as file:
            data = file.write(item)
        return data
    else:
        return None