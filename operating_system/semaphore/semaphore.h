#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>


typedef struct {
    pthread_mutex_t sem_mutex;
    pthread_cond_t sem_cond;
    unsigned int sem_count;
} sem_t;

int sem_wait(sem_t *sem);
int sem_post(sem_t *sem);

