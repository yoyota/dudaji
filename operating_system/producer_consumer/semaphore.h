#include <ntsid.h>
#include <pthread.h>

typedef struct {
    pthread_mutex_t sem_mutex;
    pthread_cond_t sem_cond;
    unsigned int sem_count;
} sem_t;

int sem_wait(sem_t *sem);
int sem_post(sem_t *sem);
int sem_init(sem_t *sem, unsigned int count);
#ifndef PRODUCER_CONSUMER_SEMAPHORE_H
#define PRODUCER_CONSUMER_SEMAPHORE_H

#endif //PRODUCER_CONSUMER_SEMAPHORE_H
