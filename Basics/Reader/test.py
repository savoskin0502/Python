from filereader import FileReader

if __name__ == '__main__':
    reader = FileReader('test.txt')
    text = reader.read()
    print(text)