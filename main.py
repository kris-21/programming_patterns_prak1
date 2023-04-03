import os
import shutil

# Запрос пути к папке
folder_path = input("Введите путь к папке с файлами: ")

# Создание папки "Прочее", если она не существует
misc_folder = os.path.join(folder_path, "Прочее")
if not os.path.exists(misc_folder):
    os.makedirs(misc_folder)

# Обработка файлов
for filename in os.listdir(folder_path):
    # Проверяем, является ли файл текстовым
    if not filename.endswith('.txt'):
        continue

    # Разделяем имя файла на части по символу подчеркивания
    parts = filename.split('_')

    # Извлекаем название отдела из первой части имени файла, если она не пустая
    if len(parts) > 1 and parts[0]:
        department_name = parts[0]
    else:
        department_name = None

    # Определяем путь к папке для отдела или для "Прочее"
    if department_name:
        department_folder = os.path.join(folder_path, department_name)
    else:
        department_folder = misc_folder

    # Создаем папку, если ее нет
    if not os.path.exists(department_folder):
        os.makedirs(department_folder)

    # Переносим файл
    src_path = os.path.join(folder_path, filename)
    dest_path = os.path.join(department_folder, filename)
    shutil.move(src_path, dest_path)

print("Файлы успешно обработаны")
