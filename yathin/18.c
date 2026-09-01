#include<stdio.h>
int main(){

    int num,i=1,count=0;
    printf("enter the number: ");
    scanf("%d",&num);
    printf("the factors of %d are: \n",num);

    for(i=1;i<=num;i++){
        if(num%i==0){
            printf("%d ",i);
            count++;
        }
    }
    if(count==2){
        printf("\n%d is a prime number",num);
    }
    else{
        printf("\n%d is not a prime number",num);
    }
    return 0;
}

