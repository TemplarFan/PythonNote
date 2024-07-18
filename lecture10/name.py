x = 100

def add(x, y):
    print("in add, ", __name__)
    return x+y

# print(add(x, x))
# print("in main process")
if __name__ == "__main__":
    print(add(x, x))
    print("in main")