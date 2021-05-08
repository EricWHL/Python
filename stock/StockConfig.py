from ExcelModule import ExcelModule

class StockConfig(object):
    def __init__(self,in_file):
        print('StockExport')
        print('input file is :' , in_file)
        
        self.in_file = in_file
        self.in_exl = ExcelModule(self.in_file)

    def monitor_tickets(self):
        print('monitor_tickets')
        return self.in_exl.read_column_data('monitor',1)

        
    def test(self):
        print('stock export module test')
        self.monitor_tickets()
