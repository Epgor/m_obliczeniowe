def main(x, e, i):
    F = []  
    F = fib_tab(F)
    ii=0
    #a=0
    #b=0
    #e=0
    maks = 0
    switch = x
    #a = float(input("podaj a: \n"))
    #b = float(input("podaj b: \n"))
    #e = float(input("podaj e: \n"))    na potrzeby szybszych testów
    a=-9
    b=-6
    #e=3
    
    n = highest_n(a, b, e, F)
    #print(n, F[n])   
    x1, x2 = calc_x1_x2(a, b, F[n])
    print(x1, x2)

    if switch == 1:
        xmax=0
        while(ii<i):
            if func(x1) > func(x2):
                b=x2
                x2=x1
                n=n-1
                x1,null = calc_x1_x2(a,b,F[n])
                print("k3", b,x1,x2)
            else:
                a=x1
                x1=x2
                n=n-1
                null,x2 = calc_x1_x2(a,b,F[n])
                print("k3-pp", a,x1,x2)
            if (abs(x2-x1)<e) | (n==1):
                xmax = (a+b)/2
                return xmax
            ii = ii+1
        xmax = (a+b)/2
        return xmax
            
    if switch == 0:
        xmin=0
        while(ii<i):
            if func(x1) < func(x2):
                b=x2
                x2=x1
                n=n-1
                x1,null = calc_x1_x2(a,b,F[n])
            else:
                a=x1
                x1=x2
                n=n-1
                null,x2 = calc_x1_x2(a,b,F[n])
            if (abs(x2-x1)<e) | (n==1):
                xmin = (a+b)/2
                return xmin
            ii = ii+1
        

def fib_tab(F):
    F.append(1)
    F.append(1)
    
    for i in range(2,100):
        F.append(F[i-1] + F[i-2])
    return F   
    

def highest_n(a, b, e, F):
    n=0 
    while((b-a)/F[n]>=(2*e)):
        n=n+1      
    n = n-1  
    return n
    
    
def func(x):
    #return pow(100-x,2)
    return 0.6*pow(x,3)+6.0*pow(x,2)+2.2*x-7.3


def calc_x1_x2(a, b, Fn):
    x1 = b-((Fn-1)/Fn)*(b-a)
    x2 = a+((Fn-1)/Fn)*(b-a)
    return x1, x2

if __name__ == "__main__":
   # print("max", main(1, 0.1, 1))
   # print("max", main(1, 0.1, 2))
   # print("max", main(1, 0.1, 3))
    
    print("max", main(1, 0.1, 4))

    #print("min", main(0))
