#include <stdio.h>
int main(){
    int a,b;
    char op;
    printf("enter two numbers: ");
    scanf("%d %d",&a,&b);
    
    printf("enter the operator:");
    scanf(" %c",&op);

    switch (op){
        case '+':
        printf("sum of a and b :%d",a+b);
        break;
        case '-':
        printf("subtraction of a and b:%d",a-b);
        break;
        case '*':
        printf("multiplication of a and b:%d",a*b);
        break;
        case '/': 
        if (b != 0){
        printf("division of a by b:%d",a/b);
        }
        else{
            printf("divison is not possible");
        }
        break;
        default:
        printf("invalid operator");
        
    }
    return 0;

    
}