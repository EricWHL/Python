from ExcelModule import ExcelModule

def excelfunc():
    exl = ExcelModule()
    print('excelfunc')
    exl.create('text.xlsx')
    names = []
    names = exl.get_sheet_names('text.xlsx')
    for item in names:
        print(item)



if __name__=="__main__":
    print("main")
    #excelfunc()
