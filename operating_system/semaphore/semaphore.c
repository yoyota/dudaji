#include <pthread.h>
#include "semaphore.h"

int sem_wait(sem_t *sem) {
    pthread_mutex_lock(&sem->sem_mutex);

    while (sem->sem_count == 0) {
        pthread_cond_wait(&sem->sem_cond, &sem->sem_mutex);
    }
    sem->sem_count--;
    pthread_mutex_unlock(&sem->sem_mutex);

    return 0;
}

int sem_post(sem_t *sem) {
    pthread_mutex_lock(&sem->sem_mutex);

    if (sem->sem_count == 0) {
        pthread_cond_signal(&sem->sem_cond);
    }
    sem->sem_count++;
    pthread_mutex_unlock(&sem->sem_mutex);

    return 0;
}

