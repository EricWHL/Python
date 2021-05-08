import os
import openpyxl

from openpyxl import load_workbook
from openpyxl.styles import colors, Font, Fill, NamedStyle
from openpyxl.styles import PatternFill, Border, Side, Alignment


class StockExport(object):
    def __init__(self,in_file):
        print('StockExport')
        print('input file is :' , in_file)
        
        self.in_file = in_file

    def get_monitor_tickets(self):
        print('get_monitor_tickets')





        
    def test(self):
        print('stock export module test')
