#include<stdio.h>
#include<stdlib.h>
int main()
{
    system("cls");
    int pin,amt,bal=75000;
    printf("Enter your pin number :");
    scanf("%d",&pin);
if(pin==1824)
 {
    { printf("Enter the amount : ");
      scanf("%d",&amt); }
      if(amt<=75000)
      { printf("please wait\n");
      printf("collect your money\n");
      printf("Balance amount is : %d",bal - amt); }
      else
      {printf("insufficient balance");}        
 }
else
{printf("wrong pin\n");
printf("please try again");}

return 0;

} 