#include<stdio.h>
int main(){

    char ch;
    printf("enter the character:");
    scanf("%c",&ch);

    if((ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')||(ch=='A' || ch=='E' || ch=='I' || ch=='O' ||ch=='U')){

        printf("character is an vowel");
    }
    else if (('a'<=ch && 'z'>=ch) || ('A'<=ch && 'Z'>=ch)){
        printf("character is consonant");
    }
    else if ('0'<=ch && '9'>=ch){
        printf("character is a number");
    }
    else{
        printf("character is a special character");
    }
    return 0;
}