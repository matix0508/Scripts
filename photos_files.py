import os
import shutil
from typing import List
from move_files import MoveApp


PHOTO_DIR = '/home/wleklinski/Pictures'
SCREENSHOTS_DIR = os.path.join(PHOTO_DIR, 'Screenshots')
MEMES_DIR = os.path.join(PHOTO_DIR, 'Memes')

TARGET_DIRS = [SCREENSHOTS_DIR, MEMES_DIR]

CATEGORIES = ['screenshot', 'meme']


if __name__ == "__main__":
    app = MoveApp(PHOTO_DIR, CATEGORIES)
    app.run()

    