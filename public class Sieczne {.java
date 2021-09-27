public class Sieczne {
 
    public static int n,p,q;
    public static double a[];
     
    //algorytm Hornera - obliczanie wartosci wielomianu
    public static double w(int k, double x) {
    if (k==n)
    return a[n];
    else
    return w(k+1,x)*x+a[k];
    }
     
    //  algorytm Show-Trauba funkcja pomocnicza s(j)
    public static double s(int j){
    return (n-j)%q;
    }
     
    //  algorytm show-Trauba funkcja pomocnicza r(j)
    public static double r(int j)   {
    if (j%q==0)
    return q;
    else
    return 0;
    }
     
    //  Algorytm Show-Trauba - glowna funkcja
    public static double T(int i, int j, double x)  {
    if (x==0)                     //by moľna by?o obliczy† pochodnĄ w punkcie x=0
    return a[j];
    else
    if (j==-1)
    return a[n-i-1]*Math.pow(x,s(i+1));
    else
    if (i==j)
    return a[n]*Math.pow(x,s(0));
    else
    return T(i-1, j-1, x)+T(i-1, j, x)*Math.pow(x,r(i-j));
    }
     
    public static double pochodna(int stopien, double punkt)    {
    if (punkt==0)
    return T(n,stopien,punkt);
    else
    return T(n,stopien,punkt)/Math.pow(punkt,stopien%q);
    }
     
    public static void main(String[] args) {
    int k,l;
    double y,z,c,d,e;
    d = 0;
     
    System.out.println("Metoda Siecznych - obliczanie zer funkcji nie liniowych\nna przykladzie wielomianow\nPodaj stopien wielomianu");
    n = Console.readInt("?");
    a = new double[n+1];
     
    if (n<2) {
    System.out.println("Za maly stopien wielomianu");
    return;
    }
     
    System.out.println("Podaj teraz kolejne wspolczynniki wielomianu.\nZaczynij od tego z najwieksza potega.");
    for(k=n; k>=0; k--) {
    a[k] = Console.readDouble("a" + k);
    }
     
    System.out.println("Podaj poczatek przedzialu");
    y = Console.readInt("?");
    System.out.println("Podaj koniec przedzialu");
    z = Console.readInt("?");
    if (z<y) {
    System.out.println("Koniec przedzialu jest mniejszy od poczatku");
    return;
    }
     
    System.out.println("Podaj liczbe iteracji");
    l = Console.readInt("?");
    p=1; q=n+1;
     
    //pierwsze dwa przyblizenia z regula falsi
    if ((pochodna(1,y)*pochodna(2,y))<0) {
    c=z;
    c=c-(w(0,c)/(w(0,y)-w(0,c)))*(y-c);
    }
    else {
    c=y;
    c=c-(w(0,c)/(w(0,z)-w(0,c)))*(z-c);
    }
     
    for (k=1; k<l-1; k++) {
    if ((w(0,c)==0)||((w(0,c)-w(0,d))==0)) {
    break;
    }
    e=c; c=c-((w(0,c)*(c-d))/(w(0,c)-w(0,d))); d=e;
    }
     
    if (w(0,c)==0) {
    System.out.println("Dokladny pierwiastek wynosi " + c);
    }
    else {
    System.out.println("Przyblizony pierwiastek wynosi " + c);
    }
     
    return;
    }
    }