def sumnum(a,b,k):

    s = 0

    for i in range(a,b+1):
        s += k ** i
    return s
    
def mainsum():
    a = 50
    b = 150
    k =2
    print("sum of %d power of numbers from  %d to %d = %d" % (k,a,b, sumnum(a,b,k)))
    
mainsum()

