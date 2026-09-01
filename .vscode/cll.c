#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *next;
};
struct node *head = NULL;
struct node *newnode;
void insertBeginning()
{
    int value;
    printf("Enter the value to be inserted: ");
    scanf("%d",&value);
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data=value;
    if (head==NULL)
    {
        head = newnode;
        newnode->next=head;
    }
    else
    {
        struct node *temp = head;
        while (temp->next!=head)
        {
            temp = temp->next;
        }
        temp->next=newnode;
        newnode->next=head;
        head=newnode;
    }
}
void insertLast()
{
    int value;
    printf("Enter the value to be inserted: ");
    scanf("%d",&value);
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data=value;
    if (head==NULL)
    {
        head = newnode;
        newnode->next=head;
    }
    else
    {
        struct node *temp = head;
        while (temp->next!=head)
        {
            temp = temp->next;
        }
        temp->next=newnode;
        newnode->next=head;
    }
}
void insertPosition()
{
    int value;
    printf("Enter the value to be inserted: ");
    scanf("%d",&value);
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data=value;
    if (head==NULL)
    {
        head = newnode;
        newnode->next=head;
    }
    else
    {
        int position;
        printf("Enter value after which new value to be inseted: ");
        scanf("%d",&position);
        struct node *temp = head;
        while (temp->data!=position)
        {
            temp = temp->next;
        }
        newnode->next = temp->next;
        temp->next = newnode;

    }
}
void display()
{
    if (head==NULL)
    {
        printf("List is empty\n");
        return;
    }
    else
    {
        struct node *temp=head;
        while (temp->next!=head)
        {
            printf("%d->",temp->data);
            temp=temp->next;
        }
        printf("%d->%d",temp->data,head->data);
        printf("\n");
    }
}
void deleteBeginning()
{
    if (head==NULL)
    {
        printf("List is empty\n");
        return;
    }
    else if(head->next==head)
    {
        head = NULL;
    }
    else
    {
        struct node *temp=head;
        while(temp->next!=head)
        {
            temp = temp->next;
        }
        head=head->next;
        temp->next=head;
    }
}
void deleteLast()
{
    if (head==NULL)
    {
        printf("List is empty\n");
        return;
    }
    else if(head->next==head)
    {
        head = NULL;
    }
    else
    {
        struct node *temp=head;
        while(temp->next->next!=head)
        {
            temp=temp->next;
        }
        temp->next = head;
    }
}
void deletePosition()
{
    if (head==NULL)
    {
        printf("List is empty\n");
        return;
    }
    else if(head->next==head)
    {
        head = NULL;
    }
    else
    {
        int position;
        printf("Enter data value of node to be deleted:");
        scanf("%d",&position);
        struct node *temp=head;
        while (temp->next != head && temp->next->data != position)
       {
             temp = temp->next;
       }
        struct node *temp1 = temp->next;
        temp->next = temp1->next;
    }
}
int main()
{
    int op;
    while(1)
    {
        printf("1.insert 2.delete 3.display 4.Exit\n");
        printf("Choose an option: ");
        scanf("%d",&op);
        switch(op)
        {
            case 1: 
            {
                int i;
                printf("1.starting 2.last 3.specific\n");
                printf("Choose type of insertion: ");
                scanf("%d",&i);
                if (i==1)
                    insertBeginning();
                else if(i==2)
                    insertLast();
                else if(i==3)
                    insertPosition();
                else 
                    printf("Invalid option choosen");
                break;
            }
            case 2: 
            {
                int i;
                printf("1.starting 2.last 3.specific\n");
                printf("Choose type of deletion: ");
                scanf("%d",&i);
                if (i==1)
                    deleteBeginning();
                else if(i==2)
                    deleteLast();
                else if(i==3)
                    deletePosition();
                else
                    printf("Invalid operator choosen.");
                break;
            }
            case 3: display();
                    break;
            case 4: exit(0);
            default: printf("Invalid operation\n");
            
        }
    }
}