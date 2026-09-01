#include <stdio.h>
int main(){

    int x,y,s;
    printf("enter values for x,y,s:");
    scanf("%d %d %d",&x,&y,&s);
    if ((x<=s && y>=s) || (y<=s && x>=s)) {
        printf("the number is in between %d and %d",x,y);
    }

    else{
        printf("the number is not in between %d and %d",x,y);
    }

    return 0;

}
