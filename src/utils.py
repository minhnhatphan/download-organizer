import os


def create_folder(root, category):
    folder_path = os.path.join(root, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
