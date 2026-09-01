#include<stdio.h>
#include<stdlib.h>
int main()
{
    system("cls");
    int n,r,reverse=0,x;
    printf("Enter the number :");
    scanf("%d",&n);
    x=n;
    while (n!=0)
    {
    r = n % 10;
    reverse = reverse * 10 + r;
    n = n / 10;
    }
    
    printf("reverse of the number is : %d\n",reverse);
    
    if ( reverse==x)
    {
        printf(" The given number is a palandrom!!!\n i,e: %d",x);
    }
    else 
    {
            printf("The entered number is not a palandrom!!!!");
    }
   
        return 0;
}                   