from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import QIcon
import time 
import json
import threading
from multiprocessing import Process, Queue

class H台窗體(QWebEngineView):
    def __init__(self,頻道):
        super().__init__()
        self.initUI(頻道)

    def 跑js(self,x):
        self.page().runJavaScript(x)

    def initUI(self,頻道):
        self.setWindowTitle('九字切')
        self.頁面=self.page()
        self.頁面.setWebChannel(頻道)
        self.load(QUrl('file:///html/index.html'))
        self.resize(1366,768)
        self.show()    

class 山彥(QObject):
    def __init__(self,出):
        self.連線=False
        self.出=出
        super().__init__()

    @pyqtSlot(str)
    def rec(self,命令):
        if 命令=='初始化': 
            self.連線=True
        if 命令=='輸出完成':
            self.出.put('輸出完成')
            # _print('輸出完成')
        elif 命令[0]=='@':
            # _print(命令)
            self.出.put(命令[1:])

class 假面():
    def write(self,s):
        s='@'+s.replace('\n','<br/>')
        輸出隊列.put(s)
        if 輸入隊列.get(True)!='輸出完成':
            raise '???'
    def read(self,s):
        pass

def 紫禁城(出,入):
    def 收取():
        while True:
            if not 彥.連線:
                time.sleep(0.1)
                continue
            item=入.get(True)
            # _print(json.dumps(item))
            if item[0]=='@':
                主窗體.跑js('顯示(%s)'%json.dumps(item[1:]))
            elif item[0]=='反':
                主窗體.跑js('輸入(%s)'%json.dumps(item[1:]))
            else:
                _print('Warning:%s is wrong.'%item)

    app = QApplication([])
    頻道 = QWebChannel()
    彥 = 山彥(出)
    頻道.registerObject('handler',彥)
    主窗體 = H台窗體(頻道)

    t = threading.Thread(target=收取)
    t.setDaemon(True)
    t.start()

    app.exec_()

#————————————————————————————————————————————————
#主進程部分

輸入隊列=Queue()
輸出隊列=Queue()
def init():
    子進程 = Process(target=紫禁城, args=(輸入隊列,輸出隊列))
    子進程.start()

_默認面=假面()
_print=print
def print(*li,**d):
    _print(*li,**d,file=_默認面)
def input(x):
    輸出隊列.put('反'+x)
    return 輸入隊列.get(True)