
def allcaps(func):
    def uppercase():
        result = func()
        return result.upper()
    return uppercase

@allcaps
def greet():
    return "hello World!"

def main():
    print(greet())

main()
