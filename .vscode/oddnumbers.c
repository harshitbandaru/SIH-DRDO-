#include<stdio.h>
	int main() {
	 int a, b, i;
	 scanf("%d%d", &a, &b);
	 if(a>b)
	 	{   
	        for(i=a ;i >= b; i--)
	            {
	                if(i % 2 != 0)
	                printf("%d ",i);
	            }
	    }        
	else if(a<b)
        {
            for(i = b;i >= a; i--)
            {
                if(i%2!=0)
                printf("%d ",i);
            }
        }
    else
        printf("Enter two different values");
	 
    return 0;
	}