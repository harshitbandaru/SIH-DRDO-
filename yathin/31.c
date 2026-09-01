#include <stdio.h>

int main() {
    int n, i, key, found = 0;
    printf("Enter array size: ");
    scanf("%d", &n);
    int a[n];

    printf("Enter elements: ");
    for(i=0; i<n; i++) scanf("%d", &a[i]);

    printf("Enter number to search: ");
    scanf("%d", &key);

    for(i=0; i<n; i++) {
        if(a[i] == key) {
            printf("Element present at index: %d", i);
            found = 1;
            break;
        }
    }

    if(!found) printf("No");
    return 0;
}