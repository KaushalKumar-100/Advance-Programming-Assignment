#include<stdio.h>
#include<stdlib.h>
void constantSpace() {
    int a = 10, b = 20, c;
    c = a + b;
    printf("Constant Space Result: %d\n", c);
}
void linearSpace(int n) {
    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }

    printf("Linear Space used for %d elements\n", n);
    free(arr);
}
void quadraticSpace(int n) {
    int **matrix = (int **)malloc(n * sizeof(int *));

    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
    }

    printf("Quadratic Space used for %d x %d matrix\n", n, n);

    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

int main() {
    int n;
    printf("Enter input size: ");
    scanf("%d", &n);

    constantSpace();
    linearSpace(n);
    quadraticSpace(n);

    return 0;
}
