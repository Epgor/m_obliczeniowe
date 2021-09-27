def func(args):
    return args[0]+2*args[1]


def calc_zj(tab, ci ,cj ,zj, cj_zj):
    for z in range(len(zj)):
        zj[z] = ci[0]*tab[0][z]+ci[1]*tab[1][z]
        
    for z in range(len(zj)):
        cj_zj[z] = cj[z]-zj[z]
        
    return zj, cj_zj


def calc_bi(bi, ai, bi_ai):
    for i in range(len(bi)):
        bi_ai[i] = bi[i]/ai[i]
    return bi_ai  


def max_cj_zj(cj_zj):
    temp = cj_zj[0]
    x = 0
    for _ in range(len(cj_zj)):
        if cj_zj[_]>temp:
            temp = cj_zj[_]
            x=_
    return temp, x #wartosc pozycja


def set_ai(tab, col, ai):
    for i in range(len(ai)):
        ai[i] = tab[i][col]
    return ai
        

def find_exit(bi_ai):
    temp = bi_ai[0]
    x = 0
    for i in range(len(bi_ai)):
        if (bi_ai[i]<temp) & (bi_ai[i] >= 0):
            temp = bi_ai[i]
            x=i
    return temp, x


def tab_mult(tab, row, col, ci, cj, bi):
    for z in range(len(tab[0])):
        tab[row][z] = tab[row][z]/tab[row][col]
    bi[row] = bi[row]/tab[row][col]
    
    for x in range(len(tab[0])):
        tab[1-row][x] = tab[1-row][x] - tab[row][x] * tab[1-row][col]
    bi[1-row] = bi[1-row] - bi[row]*tab[1-row][col]
    
    ci[row] = cj[col]
    
    return tab, bi, ci


def stop_case(cj_zj):
    #max
    for i in range(len(cj_zj)):
        if cj_zj[i] > 0:
            return False
    return True 


def main():
    '''
    𝑥1 + 𝑥2 + 𝑥3 = 10
    −2𝑥1 + 𝑥2 + 𝑥4 = 4
    '''
    
    ilosc_ograniczen = 2
    ilosc_zmiennych = 4
    
    tab = [[1,1,1,0],
           [-2,1,0,1]]
    
    bi = [10, 4]
    ci = [0,0]
    cj = [1,2,0,0]
    
    zj = [0 for i in range(ilosc_zmiennych)]
    cj_zj = [0 for i in range(ilosc_zmiennych)]
    
    ai = [0,0]
    bi_ai = [0,0]
    iter_num = 0
    while(True):
        
        zj, cj_zj = calc_zj(tab, ci ,cj ,zj, cj_zj)

    # print(zj)  
    # print(cj_zj)     
        maxcj_zj, col = max_cj_zj(cj_zj)
        #max = 2
        ai = set_ai(tab, col, ai)

        bi_ai = calc_bi(bi, ai, bi_ai)
        #print(bi_ai) 
        mult, row = find_exit(bi_ai)
    #    print(mult,row)    
        tab, bi, ci = tab_mult(tab, row, col, ci, cj, bi)

        if stop_case(cj_zj) == True:
            #return bi, func(bi)
            break
        
        print( "\nrow, col", row, col, tab[row][col],"\n")
        
        
        print("tab: \n", tab,"\nci: \n" ,ci, "\ncj: \n",\
            cj,"\nzj: \n", zj, "\ncj_zj: \n",cj_zj, "\nbi: \n",\
                bi,"\nbi_ai: \n", bi_ai, "\n\n\n")
        
        iter_num = iter_num +1
        if iter_num > 2 :
            break

        
    
main()