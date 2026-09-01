#include <stdio.h>

// 1. No Argument, No Return Value
void greet() {
    printf("Hello\n");
}

// 2. With Argument, No Return Value
void Square(int n) {
    printf("Square of %d is: %d\n", n, n * n);
}

// 3. No Argument, With Return Value
float Pi() {
    return 3.14159;
}

// 4. With Argument, With Return Value
int add(int a, int b) {
    return a + b;
}

int main() {
    greet();
    Square(5);
    printf("Pi : %0.2f\n", Pi());
    printf("Sum: %d\n", add(10, 20));
    return 0;
}