#include<stdio.h>

int GCD(int a,int b){
   while(b!=0){ 
    int temp=b;
    b = a % b;
    a = temp;
   }
   return a;
}

int LCM(int a,int b){
    return (a * b) / GCD(a,b);
}

int main(){
    int x,y;
    printf("enter two numbers:");
    scanf("%d %d",&x,&y);
    printf("LCM of %d and %d is:%d\n",x,y,LCM(x,y));
    return 0;
}