from multiprocessing import Pool
import time
import os

def tfunc(num):
    pid = os.getpid()
    for i in range(3):
        print("Process in %d with %d." % (pid, i))
        time.sleep(1)

    return str(num) +":%d" % pid

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        adds = pool.map(tfunc, (1,2,3))
        for rstr in adds:
            print(rstr)
