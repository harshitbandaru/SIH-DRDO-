#include <stdio.h>

int main() {
    int i;

    printf("use of unconditional control statements 'continue' and 'break' (Loop 1 to 10):\n");
    for (i = 1; i <= 10; i++) {
        
        if (i == 3) {
            printf("  Skipping 3 (continue)\n");
            continue; 
        }

        if (i == 7) {
            printf("  Breaking at 7 (break)\n");
            break; 
        }

        printf("  Number: %d\n", i);
    }
    return 0;
}