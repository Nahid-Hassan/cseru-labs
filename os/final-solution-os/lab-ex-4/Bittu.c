#define _GNU_SOURCE
#include <sys/ipc.h>
#include <stdio.h>
#include <sys/shm.h>
#include <string.h>
#include <sched.h>
#include <unistd.h>
#include <stdlib.h>
#include <semaphore.h>
#include <sys/wait.h>
#include <fcntl.h>
#include "rwshem.h"

int main(int argc, char const *argv[]) {
    sem_t *sem;

    /* convert string to number */
    int a = atoi(argv[0]);
    int b = atoi(argv[1]);

    sem = sem_open("/sem", O_CREAT, 0666, 1);

    sem_wait(sem);

    int x = read_from_shm();

    printf("[Bittu] - Before Subtraction [RESULT]: %d in child: %u and [CPU]: %d\n", x, getpid(), sched_getcpu());
    printf("a = %d, b = %d\n", a, b);

    int temp = a - b;
    write_to_shm(x + temp);

    int y = read_from_shm();
    printf("[Bittu] - After Subtraction [RESULT]: %d in child: %u and [CPU]: %d\n", y, getpid(), sched_getcpu());

    sem_post(sem);

}
