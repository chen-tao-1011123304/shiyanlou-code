file = open('file.txt', 'r', encoding='utf-8')

while True:
    text = file.readline()

    if not text:
        break

    print(text, end="")

file.close()













