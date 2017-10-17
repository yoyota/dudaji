#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

volatile int exclusion = 0;

void lock() {
    while (__sync_lock_test_and_set(&exclusion, 1)) {
    }
}

void unlock() {
    __sync_synchronize();
    exclusion = 0;
}

int whos_better;

void *f1(void *arg) {
    while (1) {
        lock();
        whos_better = 1;
        sleep(1);
        printf("Thread 1: thread %d is better.\n", whos_better);
        unlock();
    }
    return NULL;
}

void *f2(void *arg) {
    while (1) {
        lock();
        whos_better = 2;
        sleep(1);
        printf("Thread 2: thread %d is better.\n", whos_better);
        unlock();
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
