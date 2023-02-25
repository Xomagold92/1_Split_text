import chardet

# Путь к файлу .txt  для определения типа кодировки файла
file_path = r'D:\Mega\28_Programming\1\doc_split_text_by.txt'

# Определение кодировки файла
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())

print("Кодировка файла: ", result['encoding'])