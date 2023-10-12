import time
def timestamp(func):
    def inner():
        print(time.ctime())
        return func
    return inner




