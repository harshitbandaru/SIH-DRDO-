#include <stdio.h>
int main(){
    int a,b,c,d;
    printf("enter values of a,b,c:");
    scanf("%d %d %d",&a,&b,&c);
    d = b*b-4*a*c;

    if(a==0){
        printf("not a qudratic equation");
    }
    else if(d<0){
        printf("roots are imaginary");
    }
    else if(d==0){
        printf("roots are real and equal");
    }
    else{
        printf("roots are real anad distinct");
    }
    return 0;
}