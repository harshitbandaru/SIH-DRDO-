#include <stdio.h>
#include<ctype.h>
#include <string.h>
#define MAX 100

char stack[MAX];
int top = -1;

void push(char c) 
{
    stack[++top] = c;
}

char pop() 
{
    return stack[top--];
}

char peek() 
{
    return stack[top];
}

int precedence(char c) {
    if (c == '^')
        return 3;
    else if (c == '*' || c == '/')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}

void infixtopostfix(char* infix) 
{
    char postfix[MAX];
    int i, k = 0;
    for (i = 0; i < strlen(infix); i++) 
    {
        char c = infix[i];

        if (isalnum(c)) 
        {
            postfix[k++] = c;
        }
        else if (c == '(') 
        {
            push(c);
        }
        else if (c == ')') 
        {
            while (top != -1 && peek() != '(') 
            {
                postfix[k++] = pop();
            }
            pop(); 
        }
        else 
        {
            while (top != -1 && precedence(peek()) >= precedence(c)) {
                postfix[k++] = pop();
            }
            push(c);
        }
    }

    while (top != -1) {
        postfix[k++] = pop();
    }

    postfix[k] = '\0';
    printf("Postfix Expression: %s\n", postfix);
}

int main() {
    char infix[MAX];
    printf("Enter infix expression: ");
    scanf("%s", infix);

    infixtopostfix(infix);

    return 0;
}
