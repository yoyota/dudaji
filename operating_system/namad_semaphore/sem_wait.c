#include <errno.h>
#include <unistd.h>
#include "semaphore.h"

int sem_wait(sem_t *sem) {
    char c;

    if (sem->sem_magic != SEM_MAGIC) {
        errno = EINVAL;
        return -1;
    }

    if (read(sem->sem_fd[0], &c, 1) == 1) {
        return 0;
    }
    return -1;
}