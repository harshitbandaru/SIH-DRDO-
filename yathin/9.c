#include <stdio.h>
int main()
{
  int a,s;
  printf("enter the value of a:");
  scanf("%d",&a);

  s = a % 100;
  printf("the last two digits of a:%d\n",s);
  return 0;

}