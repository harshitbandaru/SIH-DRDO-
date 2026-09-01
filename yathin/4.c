#include <stdio.h>
int main()
{
    int a, b;
    printf("enter two numbers:");
    scanf("%d %d",&a,&b);

    printf("Addition:%d\n",a+b);
    printf("Subtraction:%d\n",a-b);
    printf("Multiplication:%d\n",a*b);
    printf("Division:%d\n",a/b);
    printf("Modulus:%d",a%b);
    return 0;

}