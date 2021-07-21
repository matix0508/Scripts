import os
import shutil
from typing import List
import inflect

p = inflect.engine()


class MoveApp:
    def __init__(self, source: str, categories=None):
        self.dir = source
        self.categories = categories
        self.target_dirs = []
        self.make_target_dirs()

    def make_target_dirs(self):
        for category in self.categories:
            self.target_dirs.append(os.path.join(self.dir, p.plural(category).capitalize()))

    def remove_white_spaces(self) -> None:
        for f in os.listdir(self.dir):
            r = f.replace(" ","-")
            if( r != f):
                os.rename(os.path.join(self.dir, f),os.path.join(self.dir, r))

    def get_orig(self, filename: str) -> str:
        return os.path.join(self.dir, filename)

    
    def get_target(self, filename: str, target: str) -> str:
        target_path = None
        for i in range(len(self.categories)):
            if target == self.categories[i]:
                target_path = self.target_dirs[i]
        if not target_path:
            raise ValueError("I hadn't anticipated that input LOL")

        return os.path.join(target_path, filename)

    def get_files(self) -> List[str]:
        output = []
        names = os.listdir(self.dir)
        for name in names:
            if os.path.isfile(os.path.join(self.dir, name)):
                output.append(name)
        return output

    
    def create_dirs(self) -> None:
        for dir in self.target_dirs:
            if not os.path.isdir(dir):
                os.mkdir(dir)

    def move_if(self, file: str, category: str) -> None:
        if category in file.lower():
            oryg = self.get_orig(file)
            target = self.get_target(file, category)
            shutil.move(oryg, target)

    def move_files(self) -> None:
        for file in self.get_files():
            for category in self.categories:
                self.move_if(file, category)

    def run(self):
        self.create_dirs()
        self.remove_white_spaces()
        self.move_files()
