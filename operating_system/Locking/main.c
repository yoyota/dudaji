#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "semaphore.h"

int whos_better;
sem_t sem = {
        PTHREAD_MUTEX_INITIALIZER,
        PTHREAD_COND_INITIALIZER,
        1
};

void *f1(void *arg) {
    while (1) {
        sem_wait(&sem);
        whos_better = 1;
        printf("");
        printf("Thread 1: thread %d is better.\n", whos_better);
        sem_post(&sem);
        sleep(1);
    }
    return NULL;
}

void *f2(void *arg) {
    while (1) {
        sem_wait(&sem);
        whos_better = 2;
        printf("");
        printf("Thread 2: thread %d is better.\n", whos_better);
        sem_post(&sem);
        sleep(1);
    }
    return NULL;
}

int main() {
    pthread_t th1, th2;

    pthread_create(&th1, NULL, f1, NULL);
    pthread_create(&th2, NULL, f2, NULL);

    /* Main will wait until th1 and th2 are finished */
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    pthread_exit(NULL);
}
