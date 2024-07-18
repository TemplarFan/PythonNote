import threading
import time

def tfunc(*num):
    for i in num:
        print("New thread ", threading.current_thread().getName(), i)
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=tfunc, args=(10, 9))
    thread.start()

    for i in range(2):
        print(threading.current_thread().getName(), i)
        time.sleep(1)