# Multi Threading
-  Thread : A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System). In simple words, a thread is a sequence of such instructions within a program that can be executed independently of other code.
-  Advantages :
   -  Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.
   -  Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.
-  Example
^
    import threading

    def print_cube(num):
        print("Cube: {}" .format(num * num * num))

    def print_square(num):
        print("Square: {}" .format(num * num))

    if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

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
^
