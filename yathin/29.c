#include<stdio.h>
int main(){
    int n=0,a[n],i;
    printf("enter size of array:");
    scanf("%d",&n);
    printf("enter the elements of the array:");
    for(i=0;i<n;i++){
    scanf("%d",&a[i]);
    }
    int l=a[0],s=a[0];
    for(i=0;i<n;i++){
        if(a[i]>l) l=a[i];
        if(a[i]<s) s=a[i];
    }
    printf("largest value:%d\n",l);
    printf("smallest value:%d\n",s);
}