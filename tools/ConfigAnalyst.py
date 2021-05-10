import json as js

class ConfigAnalyst(object):
    def __init__(self):
        self.cfg = self.loadJson('cfg.json')
        

    def loadJson(self,path):
        with open(path,'r') as cfg:
            result = js.load(cfg)
            print(result)
        return result
    
    def isDoc(self):
        if "doc" == self.cfg['feature']:
            return True
        else:
            return False
        
    def isStock(self):
        if "stock" == self.cfg['feature']:
            return True
        else:
            return False
