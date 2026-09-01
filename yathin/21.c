#include<stdio.h>
int main(){
    int i,j;
    for(i=0;i<10;i++){
        for(j=0;j<10;j++){
            if(i==3 && j==3){
                printf("found at row %d, column %d\n",i,j);
                goto end_search;
            }
        }
    }
    end_search:
    printf("search ended,ending all loops\n");
    return 0;
}
