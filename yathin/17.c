#include<stdio.h>
int main(){

    int num1,num2,i;
    printf("enter first number: ");
    scanf("%d",&num1);
    printf("enter second number: ");
    scanf("%d",&num2);      
    for(i=num1;i<=num2;i++){
        if(i%2!=0){
            printf("%d ",i);
        }
    }
    return 0;

}
