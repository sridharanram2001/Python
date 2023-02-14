import global_variable_testing as gb
import threading

thread1 = threading.Thread(target = gb.func)
thread1.start()
while True:
    print(gb.a)


