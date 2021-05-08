import tushare as ts
import threading
import time
from .StockTicket import *

class StockMonitor(object):
    def __init__(self):
        print('StockMonitor')
        ts.set_token('2a7e5987596b91c995bfaa15b9b0de0c3947ee7fd76d6dbc06e577d8')
        # 以上方法只需要在第一次或者token失效后调用，完成调取tushare数据凭证的设置，正常情况下不需要重复设置。也可以忽略此步骤，直接用pro_api('your token')完成初始化
        # 初始化pro接口
        self.pro = ts.pro_api()

    def getrealtimedata(self,ti):
        data = ts.get_realtime_quotes(ti.code)
        ti.name = data.loc[0][0]
        ti.open = float(data.loc[0][1])
        ti.price = float(data.loc[0][3])
        ti.high = float(data.loc[0][4])
        ti.low = float(data.loc[0][5])
        ti.discribe='股票编号：{}，股票名称：{}，今日开盘价：{}，当前价格：{}，今日最高价：{}，今日最低价：{}'.format(ti.code,ti.name,ti.open,ti.price,ti.high,ti.low)
        return ti


    def run(self):
        while True:
            ticketList = [
                StockTicket('300073',50.69,53.00,'','')
            ];
            for ti in ticketList:
                data = self.getrealtimedata(ti)
                print(data.discribe)
                
                time.sleep(5)

    def execute(self):
        t1 = threading.Thread(target=self.run)
        t1.start()
