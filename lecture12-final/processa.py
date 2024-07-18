from multiprocessing import Process
import time
import os

def tfunc():
    t = 10

    while True:
        print("invoking this func.")
        print("id ", os.getpid())
        time.sleep(1)
        t = t-1
        if t<0: break


if __name__ == "__main__":
    p = Process(target=tfunc)
    print("id ", os.getpid())
    p.start()