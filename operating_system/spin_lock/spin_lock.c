#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

volatile int exclusion = 0;

void lock() {
    while (__sync_lock_test_and_set(&exclusion, 1)) {
    }
}

void unlock() {
    __sync_synchronize();
    exclusion = 0;
}
