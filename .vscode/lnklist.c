#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *newnode;
struct node *head = NULL;
void insertBeginning()
{
    newnode = (struct node *)malloc(sizeof(struct node));
    int val;
    printf("Enter you value: ");
    scanf("%d",&val);
    newnode -> data = val;
    if(head == NULL)
    {
        newnode -> next = NULL;
        head = newnode;
    }
    else
    {
        newnode -> next = head;
        head = newnode;
    } 
}
void insertLast()
{
    newnode = (struct node *)malloc(sizeof(struct node));
    int val;
    printf("Enter you value: ");
    scanf("%d",&val);
    newnode -> data = val;
    if(head == NULL)
    {
        newnode -> next = NULL;
        head = newnode;
    }
    else
    {
        struct node *temp = head;
        while( temp -> next != NULL)
            temp = temp-> next;
        temp -> next = newnode;
        newnode -> next = NULL;
    }
}
void insertPosition()
{
    //newnode = (struct node *)malloc(sizeof(struct node));
    int val;
    printf("Enter the value to be inserted: ");
    scanf("%d",&val);
    newnode -> data = val;
    if(head == NULL)
    {
        newnode -> next = NULL;
        head = newnode;
    }
    else
    {
        int position;
        scanf("%d",&position);
        struct node *temp = head;
        while(temp -> data != position)
            temp = temp -> next;
        newnode -> next = temp -> next;
        temp -> next = newnode;    
    }
}
void display()
{
    if(head == NULL)
        printf("The list is empty.\n");
    else
    {
        struct node *temp = head;
        while(temp -> next != NULL)
        {
            printf("%d -> ",temp -> data);
            temp = temp -> next;
        }
        printf("%d -> ",temp -> data);
        printf("NULL\n");
    }
}
void delete()
{
    if(head == NULL)
    {
        printf("List is Empty");
        return;
    }
    else if(head -> next == NULL)
        head = NULL;
    else
        head = head;    
}
int main()
{
    int n;
    do
    {
        printf(" 1.Insert\n 2.Delete\n 3.Display\n 4.Exit\n");
        printf("Enter your option: ");
        scanf("%d",&n);
        switch(n)
        {
            case 1:
            {
                int p;
                printf("Enter the type of insertion: \n");
                printf(" 1. Insertion as the first node\n 2.Insertion as the last node\n 3.Insertion after a certain node\n");
                scanf("%d",&p);
                if(p == 1)
                    insertBeginning();
                else if(p == 2)
                    insertLast();
                else if(p==3)
                    insertPosition(); 
                else
                    printf("Invalid operator choosen");
                break;
            }
            case 2:
                delete();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);

        }
    } while (n != 4);
    
}