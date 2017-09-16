import os


class Util(object):

    def __init__(self):
        self.dir_list = ["logs", "Project/media", "Project/staticfiles"]
        self.file_list = ["logs/logfile.txt"]

    def run(self):
        for _dir in self.dir_list:
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        for file in self.file_list:
            if not os.path.exists(file):
                os.mknod(file)
