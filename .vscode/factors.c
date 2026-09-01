#include<stdio.h>
int main(){
    int i = 1, n;
    scanf("%d", &n);
    while(i<=n)
    {
        if(n % i == 0)
        printf("%d\n",i);
        i++;
    }
}