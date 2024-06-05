def count_word(filename):
 try:
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
 except FileNotFoundError:
    print("This file is dose not exits.")
 else:
    words=contents.split()
    print(len(words))

filess=("python.txt","smit_Exercise.txt")
for files in filess:
    count_word(files)