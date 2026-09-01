#include<stdio.h>
int main(){
    int n=0,a[n],i,negative=0,positive=0,even=0,odd=0,pos_sum=0,neg_sum=0,odd_sum=0,even_sum=0;
    printf("enter size of array:");
    scanf("%d",&n);
    printf("enter the elements of the array:");
    for(i=0;i<n;i++){
    scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++){
    if (a[i]<0){
        neg_sum +=a[i];
        negative++;}
    if (a[i]>0){
        pos_sum+=a[i];
        positive++;}
    if (a[i]%2==0){
        even_sum+=a[i];
        even++;}
    if (a[i]%2!=0){
        odd_sum+=a[i];
        odd++;
    }
}
    printf("positive numbers:%d (sum:%d)\n",positive,pos_sum);
    printf("negative:%d (sum=%d)\n",negative,neg_sum);
    printf("even:%d (sum:%d)\n",even,even_sum);
    printf("odd:%d (sum=%d)\n",odd,odd_sum);
    return 0;
}