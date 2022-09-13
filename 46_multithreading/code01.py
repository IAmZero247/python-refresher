# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import os

def print_cube(num):
    """
    function to print cube of given num
    """
    print("print_cube assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running print_cube: {}".format(os.getpid()))
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("print_square assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running print_square: {}".format(os.getpid()))
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))

    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,) , name='t1')
    t2 = threading.Thread(target=print_cube, args=(10,), name='t2')

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")