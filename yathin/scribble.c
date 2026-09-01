#include<stdio.h>
int main(){
    int rows,i,j,space;
    printf("rows:");
    scanf("%d",&rows);
    for(i=rows;i>=1;i--){
        for(space=0;space<rows-i;space++) printf(" ");
        for(j=i;j>=1;j--) printf("%d ",j);
        printf("\n");
    }
}