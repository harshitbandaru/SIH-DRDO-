#include <stdio.h>

int factorial(int n)
{
    int i, fact = 1;
    for(i = 1; i <= n; i++) fact = fact * i;  
    return fact;
}

int combination(int n, int r)
{
    return factorial(n) / (factorial(r) * factorial(n - r));
}

void pascaltriangle(int rows)
{
    int i, j, space;
    for(i = 0; i < rows; i++)
    {
        for(space = 1; space <= rows - i; space++)
            printf(" ");

        for(j = 0; j <= i; j++)
            printf("%d ", combination(i, j));

        printf("\n");
    }
}

int main()
{
    int rows;
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    pascaltriangle(rows);
    return 0;
}