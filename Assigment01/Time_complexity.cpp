#include <iostream>
#include <time.h>
using namespace std;

void constant_time(int n) {
    volatile int b = n * n;   // volatile prevents compiler optimization
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

    cout << "Enter value of n: ";
    cin >> n;

    // Constant time
    start = clock();
    constant_time(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    cout << "Time taken by constant: " << time_taken << " seconds\n";

    // Linear time
    start = clock();
    linear_time(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    cout << "Time taken by linear: " << time_taken << " seconds\n";

    // Quadratic time
    start = clock();
    quadratic_time(n);
    end = clock();
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    cout << "Time taken by quadratic: " << time_taken << " seconds\n";

    return 0;
}
