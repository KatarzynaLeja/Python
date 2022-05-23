import os

path = os.getcwd()

def find_pdf_size(top):
    size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.lower().endswith(".pdf"):
                size += os.path.getsize(os.path.join(root, name))

    return f'The number of bytes taken by PDF files in the directory tree is {size}.'


print(find_pdf_size(path))

