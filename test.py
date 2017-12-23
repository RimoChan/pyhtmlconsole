import htmlconsole as hc
import numpy

if __name__=='__main__':
    hc.init()
    
    hc.print('<h1>hello, world</h1>')

    name=hc.input('input your name:')
    hc.print('Hello %s!' % name)
    
    a=[1,2,3]
    hc.print(a)

    hc.print('\n------------\n')
    
    a=numpy.zeros((40,40),dtype='float')
    hc.print('<span style="color:#ff0">%s</span>' % a)
    

