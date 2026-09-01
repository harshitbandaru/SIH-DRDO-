//operations on circular queue using arrays
#include <stdio.h>
#include <stdlib.h>
#define N 5
int rear = -1,front = -1;
int a[N];
int isFull()
{
    if ((front==0 && rear==N-1)||(front==rear+1))
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
    if (front==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void enqueue(int element)
{
    if (isFull()==1)
    {
        printf("Queue is full\n");
    }
    else
    {
        rear = (rear+1)%N;
        a[rear] = element;
        if (front==-1)
        {
            front = 0;
        }
        printf("Element inserted successfully\n");
    }
}
void dequeue()
{
    if (isEmpty()==1)
    {
        printf("Queue is empty\n");
    }
    else
    {
        printf("Deleted element: %d\n",a[front]);
        if (front == rear)
        {
            front = rear = -1;
        }
        else
        {
             front = (front+1)%N;
        }
    }
}
void display()
{
    if (isEmpty()==1)
    {
        printf("Queue is empty\n");
    }
    else
    {
            int i;
            printf("Elements are: ");
            for (i=front;i!=rear;i=(i+1)%N)
            {
                printf("%d ",a[i]);
            }
            printf("%d\n",a[i]);
    }
}
void peek()
{
    if (isEmpty()==1)
    {
        printf("Queue is empty\n");
    }
    else
    {
        printf("Peek element: %d\n",a[front]);
    }
}
int main()
{
    int op,x;
    while(1)
    {
        printf("1.enqueue 2.dequeue 3.display 4.peek 5.Exit\n");
        printf("Choose an option: ");
        scanf("%d",&op);
        switch(op)
        {
            case 1: printf("Enter a element: ");
                    scanf("%d",&x);
                    enqueue(x);
                    break;
            case 2: dequeue();
                    break;
            case 3: display();
                    break;
            case 4: peek();
                    break;
            case 5: exit(0);
            default: printf("Invalid operation\n");
            
        }
    }
}
