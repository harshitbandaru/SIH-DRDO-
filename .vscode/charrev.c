#include<stdio.h>
#include<stdlib.h>
int main() {
    system("cls");
    char str[45],rev[45];
    int ind,rev_ind;
    printf("Enter str : ");
    gets(str);
    for(ind=0; str[ind]!='\0'; ind++);
    for(--ind,rev_ind=0;ind>=0;ind++,rev_ind++){
        rev[rev_ind]=str[ind];
    }
    rev[rev_ind] = '\0';
    printf("reverse of string is : %s",rev);
    return 0;
}