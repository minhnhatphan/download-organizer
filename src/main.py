from typing import Dict, List
import yaml
import os
import re
import sys
import argparse

import utils


def main(args):
    dir_path = "\\".join(os.path.dirname(
        os.path.realpath(__file__)).split("\\")[:-1])
    with open(os.path.join(dir_path, "resources/application.yml"), 'r') as f:
        conf = yaml.safe_load(f)

    target_folders = []
    files = os.listdir(args.rootdir)

    createTargetFolders(conf, args.rootdir, target_folders)

    for f in files:
        if f in target_folders:
            continue

        moved = False

        if os.path.isfile(os.path.join(args.rootdir, f)):
            _, file_extension = os.path.splitext(f)

            file_extension = re.sub(r'[^a-zA-Z]', '', file_extension).upper()
            for category in conf['target']['list']:
                if file_extension in [cat.upper() for cat in category['extensions']]:
                    utils.move(f, args.rootdir, category['name'])
                    moved = True
                    break

        if not moved:
            utils.move(f, args.rootdir, conf['target']['default']['name'])


def createTargetFolders(conf: Dict, root_path: str, target_folders: List[str]):
    utils.create_folder(root_path, conf['target']['default']['name'])
    target_folders.append(conf['target']['default']['name'])
    for category in conf['target']['list']:
        utils.create_folder(root_path, category['name'])
        target_folders.append(category['name'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-rootdir', default="")
    args = parser.parse_args()
    main(args)
