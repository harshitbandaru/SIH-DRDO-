#include <stdio.h>

int xor(int a, int b)
{
    return a ^ b;
}

int main()
{
    int n, m, i, j;

    printf("Enter data length: ");
    scanf("%d", &n);

    printf("Enter divisor length: ");
    scanf("%d", &m);

    int data[n + m - 1];
    int divisor[m];

    printf("Enter data bits: ");
    for (i = 0; i < n; i++)
        scanf("%d", &data[i]);

    printf("Enter divisor bits: ");
    for (i = 0; i < m; i++)
        scanf("%d", &divisor[i]);

    // Add zeros
    for (i = n; i < n + m - 1; i++)
        data[i] = 0;

    // Sender CRC division
    for (i = 0; i < n; i++)
    {
        if (data[i] == 1)
        {
            for (j = 0; j < m; j++)
                data[i + j] = xor(data[i + j], divisor[j]);
        }
    }

    printf("CRC Remainder: ");
    for (i = n; i < n + m - 1; i++)
        printf("%d ", data[i]);

    // Receiver Part
    int received[n + m - 1];

    printf("\nEnter received codeword: ");
    for (i = 0; i < n + m - 1; i++)
        scanf("%d", &received[i]);

    for (i = 0; i < n; i++)
    {
        if (received[i] == 1)
        {
            for (j = 0; j < m; j++)
                received[i + j] = xor(received[i + j], divisor[j]);
        }
    }

    int error = 0;

    for (i = n; i < n + m - 1; i++)
    {
        if (received[i] != 0)
        {
            error = 1;
            break;
        }
    }

    if (error)
        printf("Error Detected\n");
    else
        printf("No Error Detected\n");

    return 0;
}