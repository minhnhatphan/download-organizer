import os
import shutil


def create_folder(root: str, category: str):
    folder_path = os.path.join(root, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# https://stackoverflow.com/questions/62064573/how-to-prevent-shutil-move-from-overwriting-a-file-if-it-already-exists


def move(file_name: str, root: str, category: str):
    source = os.path.join(root, file_name)
    dest = os.path.join(root, category, file_name)
    num = 0
    while os.path.exists(dest):
        num += 1
        period = file_name.rfind('.')
        if period == -1:
            period = len(file_name)
        new_file = f'{file_name[:period]}({num}){file_name[period:]}'

        dest = os.path.join(root, category, new_file)

    shutil.move(source, dest)
