def main(x, e,i):
    a=0
    b=7
    #e=0
    maks = 0
    ii=0
    #a = float(input("podaj a: \n"))
    #b = float(input("podaj b: \n"))
    #e = float(input("podaj e: \n"))
    
    xsr = (a+b)/2

    switch = 0 #0 min, 1 max
    switch = x
    if switch == 0:
        while(True):
            L=b-a
            x1=a+(L/4)
            x2=b-(L/4)

            if func(x1) > func(xsr):
                b = xsr
                xsr = x1
            elif func(x1) <= func(xsr):
                if func(x2) > func(xsr):
                    a=xsr
                    xsr=x2
                elif func(x2) <= func(xsr):
                    a=x1
                    b=x2
            if L <= e:
                maks = xsr
                return maks

    if switch == 1:
        while(ii<i):
            L=b-a
            x1=a+(L/4)
            x2=b-(L/4)
            print("krok 2", L, x1, x2)
            if func(x1) < func(xsr):
                print("krok 3 porownanie",  func(x1), func(xsr),)
                b = xsr
                xsr = x1
                print("krok 3", b, xsr, func(x1), func(xsr))
            elif func(x1) >= func(xsr):
                if func(x2) < func(xsr):
                    print("krok 4 porownanie",  func(x2), func(xsr),)
                    a=xsr
                    xsr=x2
                    print("krok 4a",  a, xsr)
                elif func(x2) >= func(xsr):
                    print("krok 4 porownanie",  func(x2), func(xsr),)
                    a=x1
                    b=x2
                    print("krok 4b", func(x2), func(xsr), a, b)
            if L <= e:
                maks = xsr
                print("k5", L, e, maks)
                return maks
            ii = ii+1
        maks = xsr
        return maks
            


def func(x):
    return 0.6*pow(x,3)+2.8*pow(x,2)-1.5*x+1.0
 


#print(main(1, 0.0001, 5)-0.5)

#print(main(1))
def fprim(x):
    return 4.5*pow(x,2)+0.8*x-5.5

print(fprim(0.9631))
