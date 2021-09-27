import numpy as np
from scipy.optimize import fsolve as wynik

main_string = ""

def read_2v(arg_list):
    x1=arg_list[0]
    x2=arg_list[1]
    L=arg_list[2]
    f = lambda x1,x2,L: eval(main_string)
    return f(x1,x2,L)


def dfunc(X):
    dL = np.zeros(len(X))
    h = 0.000001
    for i in range(len(X)):
        dX = np.zeros((len(X)))
        dX[i] = h
        dL[i] = (read_2v(X+dX)-read_2v(X-dX))/(2*h)
    return dL

 
def main():
    #czytanie funkcji z input
    print("x**y = x do potęgi y")
    print("sqrt(x,y) = pierwiastek z x, stopnia y")
    string_temp = ""
    try:
        string_temp = (input("Podaj funkcje do zminimalizowania:\n"))
        print("Podano: \n")
        print(string_temp)
    finally:
        if string_temp != "":
            string1 = string_temp
    string_temp = ""
    try:
            string_temp = (input("Podaj funkcje ograniczenia:\n"))
            print("Podano: \n")
            print(string_temp)
    finally:
        if string_temp != "":
            string2 = string_temp
    
    string1="x1**x1 + x2**x2"
    string2="2*x1+x2-2"
    string3 = string1 + "+L*(" + string2 + ")"
    globals()['main_string'] = string3
    
    #print(string3)
    #arg_list = [3,4]
    #f = lambda x1, x2, lamb: eval(main_string)
    #result = f(4,5,2)
    #print(result)
    try:
        print("próbuję wykonać obliczenia:")
        #MAX
        X1 = wynik(dfunc, [1,1,0])
        print(X1, read_2v(X1))
    except IndexError or ValueError:
        print("Wystąpił błąd")
    
    #MIN
    ''' 
    X2 = wynik(dfunc, [-1-1,0])
    print(X2, read_2v(X2))
    '''
    

main()