#include <stdio.h>

void readMatrix(int matrix[10][10], int r, int c);
void displayMatrix(int matrix[10][10], int r, int c);
void addMatrices(int a[10][10], int b[10][10], int r, int c);
void multiplyMatrices(int a[10][10], int b[10][10], int r1, int c1, int r2, int c2);
void transposeMatrix(int matrix[10][10], int r, int c);

int main() {
    int a[10][10], b[10][10], r1, c1, r2, c2;

    printf("Enter rows and columns for Matrix A: ");
    scanf("%d %d", &r1, &c1);
    readMatrix(a, r1, c1);

    printf("Enter rows and columns for Matrix B: ");
    scanf("%d %d", &r2, &c2);
    readMatrix(b, r2, c2);

    printf("Matrix A\n");
    displayMatrix(a, r1, c1);
    printf("Matrix B\n");
    displayMatrix(b, r2, c2);

    // Addition
    if (r1 == r2 && c1 == c2) {
        addMatrices(a, b, r1, c1);
    } else {
        printf("Addition not possible.\n");
    }

    // Multiplication
    if (c1 == r2) {
        multiplyMatrices(a, b, r1, c1, r2, c2);
    } else {
        printf("Multiplication not possible.\n");
    }

    // Transpose
    printf("Transpose of Matrix A:\n");
    transposeMatrix(a, r1, c1);

    return 0;
}


void readMatrix(int matrix[10][10], int r, int c) {
    printf("Enter elements:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
}


void displayMatrix(int matrix[10][10], int r, int c) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}


void addMatrices(int a[10][10], int b[10][10], int r, int c) {
    printf("Sum of Matrices:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d\t", a[i][j] + b[i][j]);
        }
        printf("\n");
    }
}


void multiplyMatrices(int a[10][10], int b[10][10], int r1, int c1, int r2, int c2) {
    int res[10][10];
    printf("Product of Matrices:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            res[i][j] = 0;
            for (int k = 0; k < c1; k++) {
                res[i][j] += a[i][k] * b[k][j];
            }
            printf("%d\t", res[i][j]);
        }
        printf("\n");
    }
}


void transposeMatrix(int matrix[10][10], int r, int c) {
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            printf("%d\t", matrix[j][i]);
        }
        printf("\n");
    }
}