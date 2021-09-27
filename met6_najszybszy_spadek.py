def func(x,y):
    #return 10*pow(x,2)+12*x*y+10*pow(y,2)
    return pow(x,3) + 2*pow(y,2) - 3*x*y - y + 1

def pochx(x,y,h):
    return (func(x+h,y)-func(x,y))/h

def pochy(x,y,h):
    return (func(x,y+h)-func(x,y))/h

def pochx2(x,y,h):
    return (func(x+2*h,y)-2*func(x+h,y)+func(x,y))/(h*h)

def pochy2(x,y,h):
    return (func(x,y+2*h)-2*func(x,y+h)+func(x,y))/(h*h)

def pochxy(x,y,h):
    return (func(x+h,y+h)-func(x+h,y)-func(x,y+h)+func(x,y))/(h*h)	
	
	
def main(e, max_iter):
    #do sprawdzenia
    #x=10
    #y=12
    x=3
    y=2
    
    h=0.00001
    k=0 
    #e=0.00001
    
    xk=0
    yk=0
	
    while(True):
        if k >= max_iter:
            return x,y,k
        df = [(pochx(x,y,h)),(pochy(x,y,h))]

        d2f = [[pochx2(x,y,h), pochxy(x,y,h)],\
               [pochxy(x,y,h), pochy2(x,y,h)]]
        up=(df[0]*df[0]+df[1]*df[1])
        down=(df[0]*(df[0]*d2f[0][0]+df[1]*d2f[1][0])\
		+df[1]*(df[0]*d2f[0][1]+df[1]*d2f[1][1]))
        
        try:
            ak=up/down
        except ZeroDivisionError: #0/0
            ak=up/1
            
        xk=x-ak*df[0]
        yk=y-ak*df[1]
        
        '''
        print(xk)
        print(yk)
        print(abs(xk-x))
        print(abs(yk-y))
        print(abs(pochx(xk, yk, h)))
        print(abs(pochy(xk, yk, h)))
        '''
        
        if((abs(xk-x) <= e) & (abs(yk-y) <= e)) | \
            ((abs(pochx(xk, yk, h)) <= e ) & (abs(pochy(xk, yk, h)) <= e)):
            x=xk
            y=yk
            k = k+1
            return x,y,k
        else:
            x=xk
            y=yk
            k = k+1

print(main(0.1,100))
print(main(0.01,100))
print(main(0.001,100))
print(main(0.0001,100))
print(main(0.00001,100))
print(main(0.000001,100))
print("----")
print(main(0.000001,4))
print(main(0.000001,5))
print(main(0.000001,7))
print(main(0.000001,8))
print(main(0.000001,9))
print(main(0.000001,10))
