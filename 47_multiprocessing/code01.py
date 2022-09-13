#multiprocessing
import multiprocessing
import os
#print("No of cpu ->" , multiprocessing.cpu_count())

def print_cube(num):
    """
    function to print cube of given num
    """
    print("ID of process running print_cube: {}".format(os.getpid()))
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    print("ID of process running print_square: {}".format(os.getpid()))
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    print("Both processes finished execution!")

    print(p1.is_alive())
    print(p2.is_alive())

    # both processes finished
    print("Done!")