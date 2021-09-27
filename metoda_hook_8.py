import inspect
#STAŁE
#########################
#eps = 0.01
xsi = [[1,0], [0,1]]
#########################

def func(x,y):
    return pow(x,3) + 2*pow(y,2) - 3*x*y - y + 1

def trial_stage(xbb, x00, n, e, beta, eps, itera):
    xb = xbb
    x0 = x00
    #minimum narazie

    iter_num = 0
    xn = x0
    fn = 0
    while(True):
        j =1
        f0 = func(x0[0], x0[1])
        fb = func(xb[0], xb[1])   
        
        while(True):
            if iter_num>=itera:
                print("%i osiagamy w punkcie:" % func(x0[0], x0[1]))                
                return x0 
            for i in range(n):
                xn[i] = x0[i] + xsi[j-1][i]*e
            fn = func(xn[0], xn[1])
            if fn < f0:
                f0 = fn
            else:
                for i in range(n):
                    xn[i] = xn[i] - xsi[j-1][i]*e*2
                fn = func(xn[0], xn[1])
                if fn < f0:
                    f0 = fn
                else:
                    for i in range(n):
                        xn[i] = xn[i] + xsi[j-1][i]*e
            if j != n:
                j = j + 1
                iter_num = iter_num +1
            else:
                if fb > f0:
                    x0, xb = work_stage(x0, xb, xn, n)
                    iter_num = iter_num +1
                    break
                else:                  
                    if e > eps:
                        if iter_num == 0:
                            #pktstart
                            pass
                        else:
                            e=beta*e
                        for i in range(n):
                            x0[i] = xb[i]
                        iter_num = iter_num +1
                        break
                    else:
                        iter_num = iter_num +1 
                        lines = inspect.getsource(func)                     
                        print("UDAŁO SIĘ!!!\nWystarczyło zaledwie %i iteracji!!!\n" % iter_num)
                       # print("Dla zadanej funkcji:")
                       # print(lines)
                        print("%i osiagamy w punkcie:" % func(x0[0], x0[1]))
                        #print(".\n.\n.\n")                     
                        return x0
                
   


def work_stage(x00, xbb, xn, n):
    x0 = x00
    xb = xbb
    xb0 = [0,0] #temp
    for i in range(n):
        xb0[i] = xb[i]
        xb[i] = xn[i]
    for i in range(n):
        x0[i] = 2*xb[i]-xb0[i]
    
    return x0, xb

def main(eps,itera):
    xb = [3, 2]
    x0 = [3, 2]
    e = 0.5
    beta = 0.5
    n = 2
    #poszukiwane min = [1,1]
    ###########
    #print(func(xb[0], xb[1]))
    print(trial_stage(xb, x0, n, e, beta, eps,itera))
    #print(work_stage(x0, [-0.5, 1], [0, 0.5], n))
    
    
    
if __name__ == '__main__':
    #main(0.000001, 10)
    print("1 0 0.333 -0.333 B: 2")
    print("0 1 0.666 0.333  B: 8 ")
    print("------------")
    print("zj: 1 2 1.666 0.333")
    print("cj-zj: 0 0 -1.666 -0.333")