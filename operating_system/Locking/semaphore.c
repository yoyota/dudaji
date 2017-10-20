#include <pthread.h>
#include "semaphore.h"
#include "spin_lock.h"

int sem_wait(sem_t *sem) {
//    pthread_mutex_lock(&sem->sem_mutex);
    lock();
    printf("sem_count: %d in wait \n", sem->sem_count);

    while (sem->sem_count == 0) {
        unlock();
        pthread_cond_wait(&sem->sem_cond, &sem->sem_mutex);
        lock();
    }
    sem->sem_count--;
    unlock();
//    pthread_mutex_unlock(&sem->sem_mutex);

    return 0;
}

int sem_post(sem_t *sem) {
//    pthread_mutex_lock(&sem->sem_mutex);
    lock();
    printf("sem_count: %d in post\n", sem->sem_count);

    if (sem->sem_count == 0) {
        pthread_cond_signal(&sem->sem_cond);
    }
    sem->sem_count++;
    unlock();
//    pthread_mutex_unlock(&sem->sem_mutex);

    return 0;
}

