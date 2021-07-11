import os
import shutil
from typing import List


PHOTO_DIR = '/home/wleklinski/Pictures'
SCREENSHOTS_DIR = os.path.join(PHOTO_DIR, 'Screenshots')
MEMES_DIR = os.path.join(PHOTO_DIR, 'Memes')

TARGET_DIRS = [SCREENSHOTS_DIR, MEMES_DIR]

CATEGORIES = ['screenshot', 'meme']


def remove_white_spaces() -> None:
    for f in os.listdir(PHOTO_DIR):
        r = f.replace(" ","-")
        if( r != f):
            os.rename(os.path.join(PHOTO_DIR, f),os.path.join(PHOTO_DIR, r))



def get_oryg(filename: str) -> str:
    return os.path.join(PHOTO_DIR, filename)

def get_target(filename: str, target: str) -> str:
    if target == "meme":
        target_path = MEMES_DIR
    elif target == "screenshot":
        target_path = SCREENSHOTS_DIR
    else:
        raise ValueError("I don't have anticipated that input LOL")

    return os.path.join(target_path, filename)


def get_files() -> List[str]:
    output = []
    names = os.listdir(PHOTO_DIR)
    for name in names:
        if os.path.isfile(os.path.join(PHOTO_DIR, name)):
            output.append(name)
    return output

def create_dirs() -> None:
    for dir in TARGET_DIRS:
        if not os.path.isdir(dir):
            os.mkdir(dir)

def move_if(file: str, category: str) -> None:
    # print(file)
    # print(file.lower())
    if category in file.lower():
        oryg = get_oryg(file)
        target = get_target(file, category)
        print((oryg, target))
        shutil.move(oryg, target)


def move_files(files: List[str]) -> None:
    for file in files:
        for category in CATEGORIES:
            move_if(file, category)

def main() -> None:
    create_dirs()
    remove_white_spaces()
    files = get_files()
    # print(files)
    move_files(files)

if __name__ == "__main__":
    main()

    