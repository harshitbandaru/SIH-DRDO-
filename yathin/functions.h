#ifndef functions
#define functions
int factorial(int);
int factorial( int n){
    int i,fact =1;
    for(i=1;i<=n;i++){
        fact *=i;
    } return fact;
}

int factorial_rec(int);
int factorial_rec(int n){
    if ( n<=1) return 1;
    else return n*factorial_rec(n-1);
}

int prime(int);
int prime(int n){
    int i;
    if(n<=1) return 0;
    for(i=2;i <= n/2;i++){
        if ( n % i == 0) return 0;
    }
     return 1;
}

#endif