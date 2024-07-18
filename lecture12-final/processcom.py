import multiprocessing

def tfun(queue, name):
    print("put data:", name)
    queue.put(name)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=tfun, args=(queue, "NEU, 100"))
    p.start()
    p.join()

    print("get data:", queue.get())