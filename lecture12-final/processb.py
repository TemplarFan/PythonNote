from multiprocessing import Process
import time
import os

def tfunc(num):
    for i in range(3):
        print("invoking this func.")
        print("id ", os.getpid(), num)
        time.sleep(1)

if __name__ == "__main__":
    for i in range(2):
        p = Process(target=tfunc, args=(i,))
        p.start()
    print("id ", os.getpid())