#include <stdio.h>
int top = -1;
int arr[20];
int isFull(){
    if(top == 19) return 0;
    else return 1;
}
int isEmpty()
{
    if(top == -1) return 0;
    else return 1;
}
void push(char element){
    if(isFull())
    {
         top = top + 1;
         arr[top] = element;
    }
    else printf("Stack overflow problem occured\n");
}
void pop()
{
    top = top - 1;    
}
int main()
{
    char str[20];
    printf("Enter the expression that you want to find: ");
    scanf("%s", str);
    if(str[0] == ')')
        {
            printf("Parenthesis arae imbalanced");
        }
    else
    {
        for(int i = 0; str[i] != '\0'; i++)
        {
          if(str[i] == '(') push('(');
          if(str[i] == ')') pop();
        }
        if(top==-1) 
            printf("Yes the parenthesis are balanced");
        else 
            printf("Not the parenthesis are imbalanced");

    }
}