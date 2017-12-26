from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import QIcon
import time 
import json
import threading
import functools
from multiprocessing import Process, Queue

class H檯窗體(QWebEngineView):
    def __init__(self,頻道):
        super().__init__()
        self.initUI(頻道)

    def 跑js(self,x):
        self.page().runJavaScript(x)

    def initUI(self,頻道):
        self.setWindowTitle('Ｈ檯')
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
        elif 命令=='輸出完成':
            self.出.put('輸出完成')
        elif 命令[0]=='@':
            self.出.put(命令[1:])
        else:
            _print('Warning:%s!!!' %命令)

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
    主窗體 = H檯窗體(頻道)

    t = threading.Thread(target=收取)
    t.setDaemon(True)
    t.start()

    app.exec_()

#————————————————————————————————————————————————
#主進程部分


輸入隊列=Queue()
輸出隊列=Queue()
daemon=False
@functools.lru_cache(1)
def 初始化():
    子進程 = Process(target=紫禁城, args=(輸入隊列,輸出隊列))
    global daemon
    子進程.daemon = daemon
    子進程.start()

import sys
class 假面():
    def write(self,s):
        初始化()
        s='@'+s
        s=s.replace('  ','&nbsp;&nbsp;')# 一個空格不轉義……
        s=s.replace('\n','<br/>\n')
        輸出隊列.put(s)
        if 輸入隊列.get(True)!='輸出完成':
            raise '???'
    def readline(self,tip='input:'):
        輸出隊列.put('反'+tip)
        return 輸入隊列.get(True)
    def flush(self):
        pass

mask=假面()

_print=print
def print(*li,**d):
    初始化()
    _print(*li,**d,file=mask)
def input(x=''):
    初始化()
    return mask.readline(tip=x)
def pause():
    input('Press <b>ENTER</b> key to continue . . .')