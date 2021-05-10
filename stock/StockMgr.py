from .StockData import *
from .StockMonitor import *
from .StockConfig import *
from .StockExport import *
#from .StockWindow import *

class StockMgr(object):
    def __init__(self,resfile):
        print('StockMgr')
        
        self.data_ = StockData('111111111111111')
        self.config_ = StockConfig(resfile)
        self.monitor_ = StockMonitor(self.config_.monitor_tickets())
        #self.window_ = StockWindow()

    def monitor(self):
        print('========Stock Monitor========')
        self.monitor_.execute()
        
    def test(self):
        print('stock mgr test')
        self.data_.test()
        self.config_.test()
        #self.monitor()
        #self.window_.test()
