/* the fundamental datatype */
typedef struct {
    int sem_fd[2]; /* two fds: [0] for reading, [1] for writing */
    int sem_magic; /* magic number if open */
} sem_t;

#define  SEM_MAGIC 0x89674523

#ifndef SEM_FAILED
#define SEM_FAILED
#define SEM_FAILED ((sem_t *)(-1)) /* avoid compiler warning */
#endif
