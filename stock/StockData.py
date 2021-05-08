import tushare as ts
from .StockTicket import *

class StockData(object):
    def __init__(self, data):
        print('StockData:',data)
        ts.set_token('2a7e5987596b91c995bfaa15b9b0de0c3947ee7fd76d6dbc06e577d8')
        self.tick_ = StockTicket('300073',0,0,'','')
        self.proj_ = ts.pro_api()
                
    def get_history_k_data(self):
        pass
    
    def test(self):
        print('stock data interface test')
