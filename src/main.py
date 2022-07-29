from logging import root
import yaml
import os
import shutil
import re

import utils


def main():
    with open("./resources/application.yml", 'r') as f:
        conf = yaml.safe_load(f)

    target_folders = []
    files = os.listdir(conf['root-path'])

    createTargetFolders(conf, target_folders)

    for f in files:
        if f in target_folders:
            continue

        moved = False

        if os.path.isfile(os.path.join(conf['root-path'], f)):
            _, file_extension = os.path.splitext(f)

            file_extension = re.sub(r'[^a-zA-Z]', '', file_extension).upper()
            for category in conf['target']['list']:
                if file_extension in [cat.upper() for cat in category['extensions']]:
                    utils.move(f, conf['root-path'], category['name'])
                    moved = True
                    break

        if not moved:
            utils.move(f, conf['root-path'], conf['target']['default']['name'])


def createTargetFolders(conf, target_folders):
    utils.create_folder(conf['root-path'], conf['target']['default']['name'])
    target_folders.append(conf['target']['default']['name'])
    for category in conf['target']['list']:
        utils.create_folder(conf['root-path'], category['name'])
        target_folders.append(category['name'])


if __name__ == "__main__":
    main()
