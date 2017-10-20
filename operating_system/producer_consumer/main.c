#include <stdio.h>
#include <unistd.h>
#include "semaphore.h"

int whos_better;
sem_t *sem;

void *f1(void *arg) {
    whos_better = 1;
    while (1) {
        sem_wait(sem);
        printf("Thread 1 thinks thread %d is better.\n", whos_better);
        sleep(1);
        sem_post(sem);
    }

    return NULL;
}

void *f2(void *arg) {
    whos_better = 2;
    while (1) {
        sem_wait(sem);
        printf("Thread 2 thinks thread %d is better.\n", whos_better);
        sem_post(sem);
        sleep(2);

    }

    return NULL;
}

/* Main - entry point */
int main(int argc, char **argv) {
    printf("sem_init");
    pthread_t th1, th2;
    /* Initialization */

    pthread_create(&th1, NULL, f1, NULL);
    pthread_create(&th2, NULL, f2, NULL);

    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    pthread_exit(NULL);
}