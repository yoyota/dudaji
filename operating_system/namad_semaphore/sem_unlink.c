#include <unistd.h>
#include "semaphore.h"

int sem_unlink(const char* pathname) {
    return (unlink(pathname));
}
