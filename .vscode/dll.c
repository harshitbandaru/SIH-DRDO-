#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next, *prev;
};

struct node *head = NULL;
struct node *newnode;

void iab()
{
    int val;
    printf("Enter the value to be inserted: ");
    scanf("%d",&val);
    newnode = (struct node *)malloc(sizeof(newnode));
    newnode -> data = val;
    if(head == NULL)
    {
        newnode -> prev = NULL;
        newnode -> next = NULL;
        head = newnode;
    }
    else
    {
        newnode -> prev = NULL;
        newnode -> next = head;
        head = newnode;
    }
}

void ial()
{
     int val;
    printf("Enter the value to be inserted: ");
    scanf("%d",&val);
    newnode = (struct node *)malloc(sizeof(newnode));
    newnode -> data = val;
    if(head == NULL)
    {
        newnode -> prev = NULL;
        newnode -> next = NULL;
        head = newnode;
    }
    else
    {
        struct node *temp = head;
        while(temp -> next != NULL)
            temp = temp -> next;
        temp -> next = newnode;
        newnode -> prev = temp;
        newnode -> next = NULL;            
    }
}

void iap()
{
    int val;
    printf("Enter the value to be inserted: ");
    scanf("%d",&val);
    newnode = (struct node *)malloc(sizeof(newnode));
    newnode -> data = val;
    if(head == NULL)
    {
        newnode -> prev = NULL;
        newnode -> next = NULL;
        head = newnode;
    }
    else
    {
        int pos;
        printf("Enter the postion after which u want to insert: ");
        scanf("%d",&pos);
        struct node *temp = head;
        while(temp -> next != NULL)
            temp = temp -> next;
        if(newnode -> next == NULL)
        {
            newnode -> next = NULL;
            temp -> next = newnode;
            newnode -> prev = temp;
        }
        else
        {
            newnode -> next = temp -> next;
            newnode -> prev = temp;
            temp -> next = newnode;
            newnode -> next -> prev = newnode;            
        }    
    }
}

void dfn()
{
    if(head == NULL)
    {
        printf("List is empty");
        return;
    }
    else if(head -> prev == NULL && head -> next == NULL)
        head = NULL;
    else
    {
        head = head -> next;
        head -> prev = NULL;
    }
}

void dln()
{
        if(head == NULL)
    {
        printf("List is empty");
        return;
    }
    else if(head -> prev == NULL && head -> next == NULL)
        head = NULL;
    else
    {
        struct node *temp = head;
        while(temp -> next != NULL)
            temp = temp -> next;
        temp -> prev -> next = NULL;
    }
}

void dsn()
{
        if(head == NULL)
    {
        printf("List is empty");
        return;
    }
    else if(head -> prev == NULL && head -> next == NULL)
        head = NULL;
    else
    {
        int pos;
        printf("Enter the position of the node to be deleted: ");
        scanf("%d",&pos);
        struct node *temp = head;
        while(temp -> next != NULL)
            temp = temp -> next;
        temp -> next -> prev = temp -> prev;
        temp -> prev -> next = temp -> next;
    }
}

void display_from_start()
{
    if(head == NULL)
    {
        printf("List is empty!");
        return;
    }
    else
    {
        struct node *temp = head;
        while(temp -> next != NULL)
        {    
            printf("%d->",temp -> data);
            temp = temp -> next;
        }
        printf("\n");
    }
}

void display_from_end()
{
      if(head == NULL)
    {
        printf("List is empty!");
        return;
    }
    else
    {
        struct node *temp = head;
        while(temp -> next != NULL)
            temp = temp -> next;
        while(temp -> prev != NULL)
        {    
            printf("%d->",temp -> data);
            temp = temp -> prev;
        }
        printf("%d",temp -> data);
        printf("\n");
    }
}

int main()
{
    int op;
    while(1)
    {
        printf("1.Insertion\n2.Deletion\n3.Display\n4.Exit\n");
        printf("Choose an option: ");
        scanf("%d",&op);
        switch(op)
        {
            case 1: 
            {
                int i;
                printf("1.First node\n2.Last node\n3.Specific node\n");
                printf("Choose type of insertion: ");
                scanf("%d",&i);
                if (i==1)
                    iab();
                else if(i==2)
                    ial();
                else if(i==3)
                    iap();
                else 
                    printf("Invalid option choosen.");
                break;
            }
            case 2: 
            {
                int i;
                printf("1.First node\n2.Last node\n3.Specific node\n");
                printf("Choose type of deletion: ");
                scanf("%d",&i);
                if (i==1)
                    dfn();
                else if(i==2)
                    dln();
                else if(i==3)
                    dsn();
                else
                    printf("Invalid option choosen.");
                break;
            }
            case 3: 
            {   int i;
                printf("1.Display from the START\n2.Display from the END\n");
                printf("Select the sequence of Display to be performed: ");
                scanf("%d",&i);
                if(i==1)
                    display_from_start();
                else if(i==2)
                    display_from_end();
                else
                    printf("Invalid option choosen.");
                break;
            }    
            case 4: exit(0);
            default: printf("Invalid operation\n");
        }
    }
}