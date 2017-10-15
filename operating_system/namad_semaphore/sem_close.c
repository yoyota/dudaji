#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include "semaphore.h"

int sem_close(sem_t *sem) {
    if (sem->sem_magic != SEM_MAGIC) {
        errno = EINVAL;
        return (-1);
    }
    sem->sem_magic = 0;
    if (close(sem->sem_fd[0] == -1 || close(sem->sem_fd[1] == -1))) {
        free(sem);
        return -1;
    }
    free(sem);
    return 0;
}
