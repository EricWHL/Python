import os
import openpyxl

from openpyxl import load_workbook
from openpyxl.styles import colors, Font, Fill, NamedStyle
from openpyxl.styles import PatternFill, Border, Side, Alignment


class ExcelModule(object):
    def __init__(self):
        print(self)

    def create(self, path):
        print(os.path.splitext(os.path.basename(path))[0])
        if os.path.exists(path):
            return False
        else:
            wb = openpyxl.Workbook()
            wb.create_sheet(index = 0, title = os.path.splitext(os.path.basename(path))[0])
            wb.remove_sheet(wb.get_sheet_by_name('Sheet'))
            wb.save(path)
            return True

    def get_sheet_names(self, path):
        wb = load_workbook(path)
        return wb.sheetnames
    
    def add_sheet_front(self, path, sheetname):
        print('add sheet front')

    def add_sheet_end(self, path, sheetname):
        print('add sheet end!')
#    def write07Excel(path):
#       wb = openpyxl.Workbook()
#       sheet = wb.active
#       sheet.title = '2007测试表'
#
#    value = [["名称", "价格", "出版社", "语言"],
#             ["如何高效读懂一本书", "22.3", "机械工业出版社", "中文"],
#             ["暗时间", "32.4", "人民邮电出版社", "中文"],
#             ["拆掉思维里的墙", "26.7", "机械工业出版社", "中文"]]
#        for i in range(0, 4):
#            for j in range(0, len(value[i])):
#                sheet.cell(row=i+1, column=j+1, value=str(value[i][j]))
#
#       wb.save(path)
#       print("写入数据成功！")
#
#
#    def read07Excel(path):
#        wb = openpyxl.load_workbook(path)
#        sheet = wb.get_sheet_by_name('2007测试表')
#
#        for row in sheet.rows:
#            for cell in row:
#                print(cell.value, "\t", end="")
#                print()
