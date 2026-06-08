#include <pthread.h>
#include <stdio.h>

void* worker(void* arg) {
    printf("Hello from worker thread\n");
    return NULL;
}

int main() {

    pthread_t tid;

    pthread_create(&tid, NULL, worker, NULL);

    pthread_join(tid, NULL);

    printf("Back in main thread\n");

    return 0;
}