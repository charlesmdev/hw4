
def allcaps(func):
    def uppercase():
        result = func()
        return result.upper()
    return uppercase