import Global_testing as t1
import threading

#T1 = threading.Thread(target=t1.start_prog())
#T1.start()
t1.start_prog()
print(t1.recv_data)
