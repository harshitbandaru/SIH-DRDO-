#include<stdio.h>
#include<conio.h>
int main()
{
signed int a,b,c;
scanf("%d",&a);
scanf("%d",&b);
c = ~ a;
printf("%d\n",c);
printf("AND: %d\n", a & b);
printf("OR: %d\n",a | b);
printf("XOR: %d\n",a^ b);
printf("NOT a: %d\n",c);
printf("Left shift a by 1: %d\n",a<<1);
printf("Right shift a by 1: %d\n",a>>1);
}


