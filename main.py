from ExcelModule import ExcelModule
from container import Group

def excelfunc():
    exl = ExcelModule()
    print('excelfunc')
    if exl.create('text.xlsx'):
        print('create file success!')
    else:
        print('create file error!')
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
    #test()
    excelfunc()
