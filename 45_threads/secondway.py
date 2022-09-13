import time
from threading import *

class T1(Thread):

    def run(self):
        for i in range(7):
            print('Hello World', i)
            time.sleep(.5)


t1 = T1()
t1.start()
t1.join()