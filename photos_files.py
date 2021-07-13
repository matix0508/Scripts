from move_files import MoveApp


PHOTO_DIR = '/home/wleklinski/Pictures'
CATEGORIES = ['screenshot', 'meme']


if __name__ == "__main__":
    app = MoveApp(PHOTO_DIR, CATEGORIES)
    app.run()

    