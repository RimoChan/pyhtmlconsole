import os

import htmlconsole as hc
hc.daemon=True

def test_1():
    import numpy
    hc.print('<h1>hello, world</h1>')

    name=hc.input('input your name:')
    hc.print('Hello %s!' % name)
    hc.print('Hello %s!' % name)
    
    a=[1,2,3]
    hc.print(a)

    hc.print('\n--------------------------------\n')
    
    a=numpy.zeros((50,50),dtype='float')
    hc.print('<span style="color:#ff0">%s</span>' % a)
    
    hc.pause()


def test_2():
    import logging
    import sys

    sys.stdout=hc.mask
    sys.stderr=hc.mask
    sys.stdin=hc.mask
    input=hc.input

    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Print by modules!')

    s=input('input your name:')
    print('<big>%s</big>' %s)

    hc.pause()


def test_3():
    import sys
    sys.stdout=hc.mask
    sys.stderr=hc.mask
    sys.stdin=hc.mask
    input=hc.input

    import time
    import progressbar
    bar = progressbar.ProgressBar(max_value=27)
    for i in range(27):
        time.sleep(0.1)
        bar.update(i)

    hc.pause()
    

if __name__=='__main__':
    test_1()
    test_2()
    test_3()
