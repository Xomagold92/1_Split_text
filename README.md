Это скрипт на Python, который разбивает текстовый файл на фрагменты на основе указанного размера фрагмента (по умолчанию 2000 символов) и условия (ближайшая точка). Скрипт также добавляет разделитель между фрагментами с заданным количеством строк (по умолчанию 20).

Установите необходимые пакеты, выполнив команду pip install chardet.
Загрузите скрипт и сохраните его как split_text_by_length.py.
В скрипте измените переменную file_path на путь к текстовому файлу, который вы хотите разделить.
При необходимости измените переменные fragment_size и divider_count, чтобы настроить размер фрагментов и количество строк
Запустите скрипт, используя команду python split_text_by_length.py.
Новый файл с фрагментами будет сохранен с добавлением суффикса _split к исходному имени файла в том же катал
Как использовать:

Убедитесь, что у вас установлен Python. 
Если его нет, скачайте и установите с официального сайта https://www.python.org/.
Сохраните свой текстовый файл, который вы хотите разделить, в одном каsplit_text_by_length.py.
Откройте командную строку (или терминал в Linux/MacOS).
Перейдите в каталог, где находcd. Например, если файлы находятся в каталоге "D:\Mega\Documents", то нужно ввести cd D:\Mega\Documents.
Запустите программу, введя команду python split_text_by_length.py <имя вашего файла>. Например, если ваш файл называется mytext.txt, то команда будет выглядеть так: python split_text_by_length.py mytext.txt.
Программа разделит ваш файл на фрагменты и сохранит их в новом файле в том же каталоге, что и исходный файл. Имя нового файла будет иметь суффикс _split.
Готово! Теперь вы можете использовать разделенный текст в свои