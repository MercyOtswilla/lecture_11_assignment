def sumnum(a,b):

    s = 0

    for i in range(a,b+1):
        s += i
    return s
    
def mainsum():
    a = 50
    b = 150
    print("sum of numbers from %d to %d = %d" % (a,b, sumnum(a,b)))
    
mainsum()

