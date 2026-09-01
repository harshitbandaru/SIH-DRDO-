#include<stdio.h>
int main(){
    int n=0,a[n],i;
    printf("enter size of array:");
    scanf("%d",&n);
    printf("enter the elements of the array:");
    for(i=0;i<n;i++){
    scanf("%d",&a[i]);
    }
    printf("elements in array:");
    for(i=0;i<n;i++) {
        printf("%d  ",a[i]);
    }
    return 0;
}