import os
import chardet


def split_text_by_length(file_path, fragment_size=2000, divider_count=20):
    # Определяем кодировку файла
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f"Кодировка файла: {encoding}")

    # Читаем содержимое файла
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()

    # Разбиваем текст на фрагменты с учетом условия
    fragments = []
    start_index = 0
    while start_index < len(content):
        end_index = min(start_index + fragment_size, len(content))
        if end_index == len(content):
            fragments.append(content[start_index:end_index])
        else:
            prev_dot_index = content.rfind(".", start_index, end_index)
            if prev_dot_index == -1:
                fragments.append(content[start_index:end_index])
            else:
                fragments.append(content[start_index:prev_dot_index + 1])
                start_index = prev_dot_index + 1
                continue
        start_index = end_index

    # Добавляем разделитель между фрагментами с переносами строк
    divider = f"\n\n{'@' * divider_count}\n\n"
    text_with_dividers = divider.join(fragments)

    # Определяем путь и имя для нового файла
    path, ext = os.path.splitext(file_path)
    new_file_path = f"{path}_split{ext}"

    # Записываем результат в новый файл
    with open(new_file_path, 'w', encoding=encoding) as f:
        f.write(text_with_dividers)
    print(f"Новый файл сохранен по пути: {new_file_path}")


if __name__ == '__main__':
    file_path = r"D:\Mega\28_Programming\1\doc_split_text_by.txt"
    split_text_by_length(file_path, fragment_size=2000, divider_count=50)


