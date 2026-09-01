#include <stdio.h>
#include <math.h>

int main() {
    int data[20], code[20];
    int m, r = 0, n;
    int i, j, parity, error = 0;
    
    printf("Enter no. of data bits: ");
    scanf("%d", &m);
    
    while (pow(2, r) < (m + r + 1)) {
        r++;
    }
    n = m + r;
    
    printf("Enter %d data bits: ", m);
    for (i = 1, j = 0; i <= n; i++) {
        if ((i & (i - 1)) == 0) {
            code[i] = 0;
        } else {
            scanf("%d", &code[i]);
        }
    }
    
    for (i = 0; i < r; i++) {
        parity = 0;
        int pos = (1 << i);
        for (j = 1; j <= n; j++) {
            if (j & pos) {
                parity ^= code[j];
            }
        }
        code[pos] = parity;
    }
    
    printf("\nGenerated Hamming Code: ");
    for (i = n; i >= 1; i--) {
        printf("%d", code[i]);
    }
    
    printf("\nEnter error position (0 for no error): ");
    scanf("%d", &error);
    
    if (error != 0 && error <= n) {
        code[error] ^= 1;
    }
    
    printf("Received Code: ");
    for (i = n; i >= 1; i--) {
        printf("%d", code[i]);
    }
    
    int errorPosition = 0;
    for (i = 0; i < r; i++) {
        parity = 0;
        int pos = (1 << i);
        for (j = 1; j <= n; j++) {
            if (j & pos) {
                parity ^= code[j];
            }
        }
        if (parity) {
            errorPosition += pos;
        }
    }
    
    if (errorPosition == 0) {
        printf("\nNo error detected.\n");
    } else {
        printf("\nError detected at position: %d", errorPosition);
        code[errorPosition] ^= 1;
        printf("\nCorrected Code: ");
        for (i = n; i >= 1; i--) {
            printf("%d", code[i]);
        }
        printf("\n");
    }
    
    return 0;
}