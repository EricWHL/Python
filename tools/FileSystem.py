import glob
import os

class FileSystem(object):
    def __init__(self):
        pass

    def find_file_by_ext(self,ext):
        return glob.glob('*.' + ext)

    def find_files_by_path(self,path):
        return os.listdir(path)
        
    def test(self):
        print('filesystem test')
