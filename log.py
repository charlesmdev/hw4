import time

def timestamp(func):
    print(time.ctime())
    return func


@timestamp
def hi():
    print('hi')

hi()

