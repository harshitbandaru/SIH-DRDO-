#include<stdio.h>
#include<math.h>
int main(){
    int num,remainder,sum=0,originalnum,temp=0,n=0;
    printf("enter the number: ");
    scanf("%d",&num);
    originalnum=num;
    temp=num;
    while(temp!=0){
        temp=temp/10;
        n++;
    }
    temp=num;
    while(temp!=0){
        remainder=temp%10;
        sum+=pow(remainder,n);
        temp=temp/10;
    }
    if(sum==originalnum){
        printf("%d is an armstrong number",originalnum);
    }
    else{
        printf("%d is not an armstrong number",originalnum);
    }
    return 0;
}   