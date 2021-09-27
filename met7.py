def func(x,y):
    #return 10*pow(x,2)+12*x*y+10*pow(y,2)
    return 14*pow(x,2)+3*pow(y,2)-8*x*y+21*y-3

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
	
def main():

    a=-5
    b=-5
    x=a
    y=b
    i=1
    #string="warunek konieczny nie jest spe�niony"
    #jetest� funkcj� g��wn�
    #print("start")

    print("Wynik Stycznych:")
    #if(not((warun(func(a), func(b))) & (warun(func3(a), func3(b))))):
    print(x,y,0)
    while(abs(pochx(x,y,0.00001)) >= 0.05) | (abs(pochy(x,y,0.00001)) >= 0.05):
        try:
            print(i)
            x = styczna_x(y)
            print(x)
            y = styczna_y(x)
            print(y)
        except ZeroDivisionError:
            print("zerodiv")
            break
        i=i+1


def warun(x,y):
    if(x*y<0):
        return True
    else:       
        return False

            
def styczna_x(yn):
    a = -100
    b = 100
    y=yn
    x=0
    e=0.000001
    

    if(pochx2(b,y,e) >= 0) & (pochx(a,y,e) >=0):
        x=a
    else:
        x=b
    while(abs(pochx(x,y,e)) >= e):
        x=x-(pochx(x,y,e)/pochx2(x,y,e))
    return x
        
        
def styczna_y(xn):
    a = -100
    b = 100
    x=xn
    y=0
    e=0.000001
    

    if(pochy2(b,x,e) >= 0) & (pochy(x,a,e) >=0): #pochodna 3 zmienić
        y=a
    else:
        y=b
    while(abs(pochy(x,y,e)) >= e):
        y=y-(pochy(x,y,e)/pochy2(x,y,e))
                
    return y
        
      

main()

def ff(x):
    return (0.6*(pow(x,3))+6.0*(pow(x,2)+2.2*x-7.3))

