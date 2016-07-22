def myLog(x, b):
    if x < b:
        return 0  
    return 1 + myLog(x/b, b)