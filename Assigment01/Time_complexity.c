#include <stdio.h>
#include <time.h>

void constant_time(int n) {
    volatile int b = n * n;   // prevents compiler optimization
}

void linear_time(int n) {
    volatile int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += i;
    }
}

void quadratic_time(int n) {
    volatile int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            count++;
        }
    }
}

int main() {
    clock_t start, end;
    double time_taken;
    int n;

    printf("Enter value of n: ");
    scanf("%d", &n);

    // Constant time
    start = clock();
    constant_time(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken by constant: %f seconds\n", time_taken);

    // Linear time
    start = clock();
    linear_time(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken by linear: %f seconds\n", time_taken);

    // Quadratic time
    start = clock();
    quadratic_time(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken by quadratic: %f seconds\n", time_taken);

    return 0;
}
