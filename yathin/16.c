#include<stdio.h>

int main(){

    char ch,alphabet;
    printf("enter the character: ");
    scanf("%c",&ch);

    if (ch>='a' && ch<='z'){
        printf("%c",ch - 32);
    }
    
    else if (ch>='A' && ch<='Z'){
        printf("%c",ch + 32);
    }

    else 
    printf("not a alphabet");
    return 0;
}