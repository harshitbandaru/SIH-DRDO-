#include<stdio.h>
int top =-1;
int arr[20];
int isFull()
{
    if(top==19) return 0;
    else return 1;
}
void push(int element)
{
    if(isFull()){
         top = top+1;
         arr[top] = element;
    }
    else printf("Stack overflow problem occured\n");
}
int pop(){
       return arr[top--];  
}
int main(){
    char str[20];
    int k,operand2,operand1;
    printf("Enter the the postfix expression that has to be evaluated: ");
    scanf("%s",str);
    for(int i=0;str[i]!='\0';i++){
        if(str[i]>='0'&&str[i]<='9'){
            int p = str[i]-48;
            push(p);
        }
        else{
            switch(str[i]){
                case '+':{
                    operand2 = pop();
                    operand1 = pop();
                    k = operand1 + operand2;
                    push(k);
                    break;
                }
                case '-':{
                    operand2 = pop();
                    operand1 = pop();
                    k = operand1 - operand2;
                    push(k);
                    break;
                }
                case '*':{
                    operand2 = pop();
                    operand1 = pop();
                    k = operand1 * operand2;
                    push(k);
                    break;
                }
                case '/':{
                    operand2 = pop();
                    operand1 = pop();
                    k = operand1 / operand2;
                    push(k);
                    break;
                }
                case '%':{
                    operand2 = pop();
                    operand1 = pop();
                    k = operand1 % operand2;
                    push(k);
                    break;
                }
            }
        }
    }
    printf("The value of your given postfix expression is %d\n",pop());
}