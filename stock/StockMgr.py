from .StockData import *
from .StockMonitor import *
from .StockExport import *

class StockMgr(object):
    def __init__(self,resfile):
        print('StockMgr')
        
        self.data_ = StockData('111111111111111')
        self.export_ = StockExport(resfile)
        self.monitor_ = StockMonitor()

    def monitor(self):
        print('========Stock Monitor========')
        self.monitor_.execute()
        
    def test(self):
        print('stock mgr test')
        self.data_.test()
