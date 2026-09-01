#include <stdio.h>
#include <stdlib.h>
void push(int x,int a[],int n);
void pop(int a[]);
void display(int a[]);
int isEmpty();
int isFull(int n);  
void peek(int a[]);
int top = -1;
int main()
{
    int n,x;
    printf("Enter size: ");
    scanf("%d",&n);
    int a[n];
    int op;
    while(1)
    {
        printf("1.push 2.pop 3.display 4.peek 5.Exit\n");
        printf("Choose an option: \n");
        scanf("%d",&op);
        switch(op)
        {
            case 1: 
                    printf("Enter a element: ");
                    scanf("%d",&x);
                    push(x,a,n);
                    break;
            case 2: 
                    pop(a);
                    break;
            case 3: 
                    display(a);
                    break;
            case 4: 
                    peek(a);
                    break;
            case 5: 
                    exit(0);
            default: 
                    printf("Invalid operation");
            
        }
    }
}
int isFull(int n)
{
    if (top == n-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int isEmpty()
{
    if (top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void push(int x,int a[],int n)
{
    if (isFull(n)==1)
    {
        printf("Stack is full\n");
    }
    else
    {
        a[++top] = x;
        printf("Element pushed successfully\n");
    }
}
void pop(int a[])
{
    if (isEmpty()==1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Popped element: %d\n",a[top--]);
    }
}
void display(int a[])
{
    if (isEmpty()==1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Elements are: ");
        for (int i=top;i>=0;i--)
        {
            printf("%d ",a[i]);
        }
        printf("\n");
    }
}
void peek(int a[])
{
    if (isEmpty()==1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Peek element: %d\n",a[top]);
    }
}