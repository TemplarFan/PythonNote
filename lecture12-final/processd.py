from multiprocessing import Pool
import time
import os

def tfunc():
    for i in range(3):
        print(i)
        time.sleep(1)



if __name__ == "__main__":
    pool = Pool(2)
    for i in range(3):
        pool.apply_async(tfunc)


    pool.close()
    pool.join()
    # pool.terminate()