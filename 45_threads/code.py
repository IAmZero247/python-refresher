import  time
import threading
# https://www.youtube.com/watch?v=IEEhzQoKtQU
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

start = time.perf_counter()

#Function with no parameter
def printHelloWorldGreen():
    for i in range(5):
        print(style.GREEN + "Hello, World!")
        time.sleep(.5)

#Function with no parameter - this is invoked 10 times using normal python logic
def printHelloWorldYellow ():
    for i in range(5):
        print(style.YELLOW + "Hello, World!")
        time.sleep(1)

#Function with no parameter with parameter
def printHelloWorldCyan (helloCount):
    for i in range(helloCount):
        print(style.CYAN + "Hello, World!")
        time.sleep(.7)
"""
Comment thread codes and run below 2 line, note the time
#printHelloWorldYellow()
#printHelloWorldCyan()
"""

t1 = threading.Thread(target=printHelloWorldGreen)
t3 = threading.Thread(target=printHelloWorldCyan, args=[7])
pool = []
for i in range(40):
    t2= threading.Thread(target=printHelloWorldYellow)
    t2.start()
    pool.append(t2)

t1.start()
t3.start()

pool.append(t1)
pool.append(t3)

for t in pool:
       t.join()

end = time.perf_counter()

print(style.RESET + str( round(end-start, 2)))