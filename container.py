
class Group(object):
    __len = 0
    
    def __init__(self):
        print(self.__len)

    def get_len(self):
        return len

    def append(self, data):
        self.__len = self.__len +1
        print(self.__len)
