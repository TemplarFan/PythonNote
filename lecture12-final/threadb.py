import threading
import time

class MyThread(threading.Thread):
    def __init__(self, num):
        self.num = num
        threading.Thread.__init__(self)

    def run(self):
        for i in self.num:
            print("New thread ", threading.current_thread().getName(), i)
            time.sleep(1)

if __name__ == "__main__":
    thread = MyThread((10,9))
    thread.start()

    for i in range(2):
        print(threading.current_thread().getName(), i)
        time.sleep(1)