# coding=gbk
from ExcelModule import ExcelModule
from container import Group
from stock.StockMgr import *


def excelfunc():
    exl = ExcelModule()
    print('excelfunc')
    if exl.create('total.xlsx'):
        print('create file success!')
    else:
        print('create file error!')
    names = []
    names = exl.get_sheet_names('total.xlsx')
    for item in names:
        print(item)

    exl.copy_sheet('./res/Desay_C100_Cluster_FunctionTest_ADAS_V1.0.xlsx','total.xlsx','统计','ADAS_统计')
    exl.copy_sheet('./res/Desay_C100_Cluster_FunctionTest_BASIC_V1.0.xlsx','total.xlsx','统计','BASIC_统计')
    exl.copy_sheet('./res/Desay_C100_Cluster_FunctionTest_TT Priority_V1.0.xlsx','total.xlsx','统计','TT Prority_统计')

def test():
    gp = Group()
    print(gp.append('a'))
    print('test')

def st_test():
    print('st_test')
    st = StockMgr()
    st.test()


if __name__=="__main__":
    print('main')
    print(dir())
    #test()
    st_test()
    #excelfunc()
