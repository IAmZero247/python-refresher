import  time
import threading

def printHelloWorldGreen():
    for i in range(10):
        print("Hello, World!", i)
        time.sleep(.5)

t1 = threading.Thread(target=printHelloWorldGreen)
t1.start()

t1.join()
