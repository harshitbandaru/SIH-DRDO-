#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a;
    float b;
    char c;
    double d;
    printf("Enter integer:");
    scanf("%d",&a);
    printf("Enter float number:");
    scanf("%f",&b);
    printf("Enter char:");
    fflush(stdin);
    scanf("%c",&c);
    printf("Enter double value:");
    scanf("%lf",&d);
    printf("entered values:");
    printf("Integer:%d\n",a);
    printf("Float:%f\n",b);
    printf("Character:%c\n",c);
    printf("Double:%lf\n",d);
    return 0;

}