import os

def write(filename, text):
    with open(filename, "w") as file:
        file.write(text)
        file.flush()

def destroy(filename):
    if os.path.exists(filename) and os.path.isfile(filename):
        os.remove(filename)

def text_or_none(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    
    return None