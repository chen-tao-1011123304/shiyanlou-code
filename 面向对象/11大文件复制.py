file_read = open('write.txt', encoding='utf-8')
file_write = open('write1.txt', 'w', encoding='utf-8')

while True:
    text = file_read.readline()

    if not text:
        break

    file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()










