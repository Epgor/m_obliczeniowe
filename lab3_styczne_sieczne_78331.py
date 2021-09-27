#2x^3+6,5x^2-5x+6
#6x^2+13x-5
#12x+13
#12
#(-4, -2)

def main(e,i):

    a=-9
    b=-6
    string="warunek konieczny nie jest spełniony"
    #jetestę funkcją główną
    #print("start")

            
    print("Wynik Siecznych:")
    print(sieczna(a, b, e, i),  "\n")

    
    
def func(x):
    return (0.6*(pow(x,3))+6.0*(pow(x,2)+2.2*x-7.3))

def func2(x):
    return 1.8*(pow(x,2)+12*x+2.2)

def func3(x):
    return 12

def warun(x,y):
    if(x*y<0):
        return True
    else:       
        return False


def bisekcja(aa, bb, e):
    #przedział a, b oraz dokładność e
    a=aa
    b=bb
    while(1):
        xsr = (a+b)/2
        if(func(xsr))==0:
            return xsr
        else:
            if warun(func(xsr),func(a)):
                b=xsr
            else:
                a=xsr
        if abs(func(xsr))<e:
            return xsr
            
def styczna(aa, bb, e,i):
    a = aa
    b = bb
    ii=0
    xn = 0
    xn1 = 0
    if not(warun(func3(a), func(a))):
        xn = a
    else:
        xn = b
    while(ii<i):
        xn1 = xn - (func(xn)/func2(xn))
        if (abs(func(xn1))<e) | (abs(xn1-xn)<e):
            return xn1
        else:
            xn = xn1
        ii = ii+1
    return xn1    
  
def sieczna(aa, bb ,e,i):
    a = aa
    b = bb
    ii=0
    if not(warun(func(a), func3(a))):
        xn = b
        xn1 = 0
        while(ii<i):
            print(xn,func2(xn)," a:", func2(a))
            xn1 = xn-((func2(xn)/(func2(xn)-func2(a)))*(xn-a))
            print(xn1)
            if (abs(func(xn1))<e) | (abs(xn1-xn)<e):
                print("warunek")
                return xn1
            else:
                xn = xn1
            ii = ii+1
        print("iteracja ostatnia")
        return xn1
    else:
        xn = a
        xn1 = 0
        while(ii<i):
            print(xn,func2(xn)," b:", func2(b))
            xn1 = xn-((func2(xn)/(func2(xn)-func2(b)))*(b-xn))
            print(xn1)
            if (abs(func(xn1))<e) | (abs(xn1-xn)<e):
                print("warunek")
                return xn1
            else:
                xn = xn1
            ii = ii+1
        print("iteracja ostatnia")
        return xn1

        
        
        
   

main(0.0001, 4)
print(func2(-9))

