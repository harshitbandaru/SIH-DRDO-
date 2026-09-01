
#include<stdio.h>
#include<stdlib.h>
int main()
{
    system("cls");
    char op;
    float n1,n2;
    printf("Enter the operator ( + , - , * , / ) :");
    scanf("%c",&op);
    printf("Enter the two operands:");
    scanf("%f%f",&n1,&n2);    
      switch (op) 
  {
    case '+':
      printf("%.1f + %.1f = %.1f", n1, n2, n1 + n2);
      break;
    case '-':
      printf("%.1f - %.1f = %.1f", n1, n2, n1 - n2);
      break;
    case '*':
      printf("%.1f * %.1f = %.1f", n1, n2, n1 * n2);
      break;
    case '/':
      printf("%.1f / %.1f = %.1f", n1, n2, n1 / n2);
      break;
    default:
      printf("Syn error!!!!");
  }
    
    return 0;
}