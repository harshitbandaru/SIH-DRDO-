#include<stdio.h>
#include "functions.h"

int main(){
    int num = 10;
    printf("Factorial (Iterative): %d\n", factorial(num));
    printf("Factorial (Recursive): %d\n", factorial_rec(num));
    if(prime(num))   printf("%d is a prime Number\n", num);        
    else printf("%d is not a prime Number\n", num);
    return 0;  
}