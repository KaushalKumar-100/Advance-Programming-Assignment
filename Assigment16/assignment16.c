 /*Develop a multithreaded C program using POSIX threads where multiple threads coordinate
  access to a shared resource using either semaphores or condition variables.
  You may implement a simple producer-consumer system, limited resource access system, or thread scheduling simulation.
The program should ensure that threads wait correctly when the resource is unavailable and continue execution only when signaled.
Demonstrate proper synchronization, safe shared-memory access, and thread communication using functions such as 
sem_wait(), sem_post(), pthread_cond_wait(), or pthread_cond_signal(). Print messages showing thread execution order 
and explain how synchronization prevents inconsistent behavior.*/


#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];

int count = 0;

pthread_mutex_t lock;

sem_t empty;
sem_t full;

void* producer(void* arg) {

    for(int i = 1; i <= 10; i++) {

        sem_wait(&empty);

        pthread_mutex_lock(&lock);

        buffer[count] = i;

        printf("Producer produced item %d\n", i);

        count++;

        pthread_mutex_unlock(&lock);

        sem_post(&full);

        sleep(1);
    }

    return NULL;
}

void* consumer(void* arg) {

    for(int i = 1; i <= 10; i++) {

        sem_wait(&full);

        pthread_mutex_lock(&lock);

        int item = buffer[count - 1];

        count--;

        printf("Consumer consumed item %d\n", item);

        pthread_mutex_unlock(&lock);

        sem_post(&empty);

        sleep(2);
    }

    return NULL;
}

int main() {

    pthread_t p, c;

    pthread_mutex_init(&lock, NULL);

    sem_init(&empty, 0, BUFFER_SIZE);

    sem_init(&full, 0, 0);

    pthread_create(&p, NULL, producer, NULL);

    pthread_create(&c, NULL, consumer, NULL);

    pthread_join(p, NULL);

    pthread_join(c, NULL);

    pthread_mutex_destroy(&lock);

    sem_destroy(&empty);

    sem_destroy(&full);

    return 0;
}