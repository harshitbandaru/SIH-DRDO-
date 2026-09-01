#include<stdio.h>
#include<stdlib.h>
int main(){
    system("cls");
    int n,q,r,n2=0;
    printf("Enter the number :");
    scanf("%d",&n);
    while (n>0){
    r = n % 10;
    n2 = n2 * 10 + r;
    n = n / 10;}
    printf("reverse of the number is : %d",n2);
    return 0;
}