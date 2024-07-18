import multiprocessing

def proc(p, name):
    print(multiprocessing.current_process().pid, "data:", name)
    p.send(name)


if __name__ == "__main__":
    con1, con2 = multiprocessing.Pipe()
    p = multiprocessing.Process(target=proc, args=(con1, "NEU, 100",))

    p.start()
    p.join()

    print(multiprocessing.current_process().pid, "get data:")
    print(con2.recv())
    