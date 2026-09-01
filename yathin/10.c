#include <stdio.h>
int main()
{
    int a,b,c,greatest;
    printf("enter three numbers:\n");
    scanf("%d %d %d",&a,&b,&c);
    
    greatest = (a > b) ? (a > c ? a : c) : (b > c ? b : c);

    printf("the greatest number is:%d\n",greatest);
    
    return 0;

}






