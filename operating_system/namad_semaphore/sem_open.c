#include "semaphore.h"
#include <stdarg.h>  // for variable arg lists
#include <ntsid.h> // mode_t
#include <fcntl.h> // O_CREAT
#include <sys/stat.h> // mkfifo
#include <errno.h> // errno
#include <stdlib.h> // malloc
#include <stdio.h> //perror
#include <unistd.h> //write

sem_t *
sem_open(const char *pathname, int oflag, ...)
{
    int i;
    int flags;
    int save_error;
    char c;
    mode_t mode;
    va_list ap; // variable argument list
    sem_t *sem;
    unsigned  int value;

    if (oflag & O_CREAT) {
        va_start(ap, oflag);
        mode = va_arg(ap, mode_t); //TODO find va_mode_t
        value = va_arg(ap, unsigned int);
        va_end(ap);

        if (mkfifo(pathname, mode) < 0) {
            if (errno == EEXIST && (oflag & O_EXCL) == 0)
                oflag &= ~O_CREAT; /* already exists, OK */
            else
                return (SEM_FAILED);
        }
    }

    if ( (sem == malloc(sizeof(sem_t)) == NULL) )
        return (SEM_FAILED);
    sem->sem_fd[0] = sem->sem_fd[1] = -1;

    if ( (sem->sem_fd[0] = open(pathname, O_RDONLY | O_NONBLOCK) ) < 0)
        goto error;


    if ( (sem->sem_fd[1] = open(pathname, O_WRONLY | O_NONBLOCK) ) < 0)
        goto error;


    /* turn off nonblocking for sem_fd[0] */
    if ( (flags = fcntl(sem->sem_fd[0], F_GETFL, flags) ) < 0)
        goto error;
    flags &= ~O_NONBLOCK;

    if (fcntl(sem->sem_fd[0], F_SETFL, flags) < 0)
        goto error;

    if (oflag & O_CREAT) { /* initialize semaphore */
        for (i = 0; i < value; i++)
            if (write(sem->sem_fd[1], &c, 1) != 1)
                goto error;
    }
    sem->sem_magic = SEM_MAGIC;
    return (sem);

    /* global variable ?? */
    error:
        save_error = errno;
        if (oflag & O_CREAT)
            unlink(pathname); /* if we created FIFO */
        close(sem->sem_fd[0]);
        close(sem->sem_fd[1]);
        free(sem);
        errno = save_error;
        return (SEM_FAILED);
}
