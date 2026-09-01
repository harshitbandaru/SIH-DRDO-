#include<stdio.h>
int main()
   {
    int a,b;
    printf("enter two numbers:");
    scanf("%d %d",&a,&b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("numbers after swapping:%d %d\n",a,b);
    return 0;

   }