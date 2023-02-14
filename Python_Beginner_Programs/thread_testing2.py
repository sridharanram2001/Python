import thread_testing as thread_val

    
def print_thread():
    print(thread_val.a)

if __name__ == "__main__":
    thread1 = Thread( target=thread1, args=("Thread-1", ) )
    thread2 = Thread( target=thread2, args=("Thread-2", ) )
    thread3 = Thread( target=print_thread )
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    
