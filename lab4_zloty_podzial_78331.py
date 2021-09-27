
def f(x):
    #funkcja do zadań
    return 2*x**3+6.5*x**2-5*x+6

def max(aa, bb, xx1, xx2, k, e, i):
    a=aa
    b=bb 
    x1=xx1
    x2=xx2
    ii=0
    #while(True):
    while(ii<i):
        if f(x1) > f(x2):
            b=x2
            x2=x1
            x1=b-k*(b-a)
        else:
            a=x1
            x1=x2
            x2=a+k*(b-a)
        if abs(x2-x1) < e:
            return (a+b)/2
        ii=ii+1
    return (a+b)/2


def min(aa, bb, xx1, xx2, k, e):
    a=aa
    b=bb 
    x1=xx1
    x2=xx2
    while(True):
        if f(x1) < f(x2):
            b=x2
            x2=x1
            x1=b-k*(b-a)
        else:
            a=x1
            x1=x2
            x2=a+k*(b-a)
        if abs(x2-x1) < e:
            return (a+b)/2


def main():
    #def zminnych
    a = -4
    b=-2
   # e=0.0001
    k=(pow(5,1/2)-1)/2

    x1=b-k*(b-a)
    x2=a+k*(b-a)
    
   # print(max(a, b, x1, x2, k, 0.1))
    #print(max(a, b, x1, x2, k, 0.01))
    #print(max(a, b, x1, x2, k, 0.001))
    #print(max(a, b, x1, x2, k, 0.0001))
    print(max(a, b, x1, x2, k, 0.00001, 3))
    print(max(a, b, x1, x2, k, 0.00001, 5))
    print(max(a, b, x1, x2, k, 0.00001, 7))
    print(max(a, b, x1, x2, k, 0.00001, 10))
    print(max(a, b, x1, x2, k, 0.00001, 20))
    print(max(a, b, x1, x2, k, 0.00001, 30))
    print(max(a, b, x1, x2, k, 0.00001, 100))
    #print(max(a, b, x1, x2, k, 0.000001))
   # print(max(a, b, x1, x2, k, 0.0000001))
    #print(min(a, b, x1, x2, k, e))

if __name__ == "__main__":    
    main()