from ExcelModule import ExcelModule
from container import Group

def excelfunc():
    exl = ExcelModule()
    print('excelfunc')
    exl.create('text.xlsx')
    names = []
    names = exl.get_sheet_names('text.xlsx')
    for item in names:
        print(item)

def test():
    gp = Group()
    print(gp.append('a'))
    print('test')

if __name__=="__main__":
    print("main")
    test()
