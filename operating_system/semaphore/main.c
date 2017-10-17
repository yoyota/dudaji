#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


typedef struct {
    pthread_mutex_t *sem_mutex;
    pthread_cond_t *sem_cond;
    unsigned int sem_count;
} sem_t;

int sem_init(sem_t *sem) {
    sem->sem_count = 1;
    sem->sem_cond = (pthread_cond_t *) malloc(sizeof(pthread_cond_t));
    sem->sem_mutex = (pthread_mutex_t *) malloc(sizeof(pthread_mutex_t));
    pthread_mutex_init(sem->sem_mutex, NULL);
    pthread_cond_init(sem->sem_cond, NULL);

    return 0;
}

int sem_wait(sem_t *sem) {
    pthread_mutex_lock(sem->sem_mutex);

    while (sem->sem_count == 0) {
        pthread_cond_wait(sem->sem_cond, sem->sem_mutex);
    }
    sem->sem_count--;
    pthread_mutex_unlock(sem->sem_mutex);

    return 0;
}

int sem_post(sem_t *sem) {
    pthread_mutex_lock(sem->sem_mutex);

    if (sem->sem_count == 0) {
        pthread_cond_signal(sem->sem_cond);
    }
    sem->sem_count++;
    pthread_mutex_unlock(sem->sem_mutex);

    return 0;
}

sem_t *sem;
int whos_better;

void *f1(void *arg) {
    while (1) {
        sem_wait(sem);
        whos_better = 1;
        printf("");
        printf("Thread 1: thread %d is better.\n", whos_better);
        sem_post(sem);
        sleep(1);
    }
    return NULL;
}

void *f2(void *arg) {
    while (1) {
        sem_wait(sem);
        whos_better = 2;
        printf("");
        printf("Thread 2: thread %d is better.\n", whos_better);
        sem_post(sem);
        sleep(1);
    }
    return NULL;
}

int main() {
    sem = (sem_t *) malloc(sizeof(sem_t));
    sem_init(sem);

    pthread_t th1, th2;

    pthread_create(&th1, NULL, f1, NULL);
    pthread_create(&th2, NULL, f2, NULL);

    /* Main will wait until th1 and th2 are finished */
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    pthread_exit(NULL);
}
