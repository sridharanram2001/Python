import threading
def func1():
    while True:
        print("func1")
        print("\n")

def func2():
    while True:
        print("func2")
        print("\n")

if __name__ == "__main__":

    thread1 = threading.Thread(target = func1)
    thread2 = threading.Thread(target = func2)
    thread1.start()
    thread2.start()
