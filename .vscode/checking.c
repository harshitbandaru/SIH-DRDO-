#include<stdio.h>
int main()
{
    int a;
    printf("Enter an Integer: ");
    scanf("%d",&a);
    if(a>0)
    {
        printf("The entered Integer '%d' is a positive integer",a);
    }
    else if(a<0)
    {
        printf("The entered Integer '%d' is a negative integer",a);
    }
    else
    {    
        printf("The entered integer is a zero '%d' ");

    }
}    