from threading import Thread
import time
a = 0  #global variable

def thread1(threadname):
    while True:
        pass
    pass

        #print(a)

def thread2(threadname):
    global a 
    while 1:
        a += 1
        time.sleep(1)

thread1 = Thread( target=thread1, args=("Thread-1", ) )
thread2 = Thread( target=thread2, args=("Thread-2", ) )

thread1.start()
thread2.start()
thread1.join()
thread2.join()
