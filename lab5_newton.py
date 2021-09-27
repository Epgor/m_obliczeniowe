
def func(x,y):
    #return 10*pow(x,2)+12*x*y+10*pow(y,2) #funkcja do spprawdzenia - o dziwo działa :D
    return pow(x,3) + 2*pow(y,2) - 3*x*y - y + 1   #moja funkcja -> 45.

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
    #moje
    x=3
    y=2
    
    h=0.00001
    k=0 #idk
    #e=0.000001
    
    xk=0
    yk=0
    
    while(True):
        
        if k >= max_iter:
            print("\n\nWynik końcowy: \n")
            return xk,yk,k
        print("=======================================\n++++++++++++++++++++++++++++\n=========================================")
        print("\nIteracja: ", k+1, "\n")
        df = [(pochx(x,y,h)),(pochy(x,y,h))]

        d2f = [[pochx2(x,y,h), pochxy(x,y,h)],\
               [pochxy(x,y,h), pochy2(x,y,h)]]
        print("grad f")
        print(df, "\n")
        print("grad^2f")
        print(d2f[0], "\n", d2f[1], "\n")

    
        divider = (d2f[0][0]*d2f[1][1]) - (d2f[0][1]*d2f[1][0])
        print("Dzielnik: (", d2f[0][0], ") * (", d2f[1][1], "- ", d2f[0][1]*d2f[1][0], ") = ", divider)
        #d*dfx-b*dfy <=gora 
        up = (d2f[1][1]*df[0])-(d2f[0][1]*df[1])
        print("")
        print("Górna część wyrażenia: ")
        print("( ",d2f[1][1], "*", df[0]," ) - ( ", d2f[0][1]," * ",df[1]," ) = ", up)
        up=up/divider
        print("gorna czesc po dzieleniu /dzielnik: ", up)
        #-c*dfx+a*dfy <=dół
        down = (d2f[0][0]*df[1]) - (d2f[1][0]*df[0])
        print("")
        print("Dolna część wyrażenia: ")
        print(" ( ", d2f[0][0], " * ", df[1], " ) - ( ",d2f[1][0]," * ",df[0]," ) = ", down)
        down = down/divider
        print("dolna czesc po dzieleniu /dzielnik: ", down)
        print("")

        xk=x-up
        print("xk = ",xk, " = x (", x,") - gora (", up, ")\n"  )
        yk=y-down
        print("yk = ", yk, " = y (", y,") - dol (", down, ")\n"  )
        print("Warunki:")
        print("xk-k | yk-k ")
        print(abs(xk-x), " | ",abs(yk-y))
        print("\npoch(xk-k) | poch(yk-k) ")
        print(abs(pochx(xk,y,h))," | ",abs(pochy(x,yk,h)))
        if ((abs(xk-x) <= e) & (abs(yk-y) <= e)) | \
            ((abs(pochx(xk,y,h)) <= e ) & (abs(pochy(x,yk,h)) <= e)):
            x=xk
            y=yk
            k = k+1
            print("\n\nWynik końcowy: \n")
            return xk,yk,k
        else:
            x=xk
            y=yk
            k = k+1
        
        
        #aktualizacja danych

        
        #warunek stopu
               
#xk, yk, k  

'''
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
'''
print(main(0.00001,5))

#łapię ekstremum w (0.9799498746867168, 0.9849624060150375) <- chyba w miarę dokładne :P
#dla k = 4
