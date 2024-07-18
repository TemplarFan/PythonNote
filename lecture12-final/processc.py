import os
import time

from multiprocessing import Process

class NewProcess(Process):
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):
        print("invoking this func.")
        print("id ", os.getpid(), self.num)
        time.sleep(1)

if __name__ == "__main__":
    for i in range(20):
        p = NewProcess(i)
        p.start()
    print("id ", os.getpid())