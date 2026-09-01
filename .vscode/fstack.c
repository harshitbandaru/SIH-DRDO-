#include<stdio.h>
int a[50];
int top = -1;
void push(int n)
{
    a[++top] = n;
}
void pop()
{
    top--;
}
int fact()
{
    return a[top];
}
int main() {
    int n;
    scanf("%d",&n);
    push(3);
    for(int i=2; i<=n;i++){
        push(fact()*i);
    }
    printf("factorial of %d is %d",n, fact());
    
    return 0;
}