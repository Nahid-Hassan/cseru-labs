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

int main(int argc, char *argv[])
{
    sem_t *sem;

    // sem_t *sem = *(int)argv[3];
    int a = atoi(argv[0]);
    int b = atoi(argv[1]);

    pid_t pid;
    // int a, b, result, shmid, i, check;

    // named semaphore is created using sem_open
    sem = sem_open("/named_semaphore", O_CREAT, 0666, 1);
    if (sem == SEM_FAILED)
    {
        printf("Semaphore error\n");
        exit(-1);
    }

    sem_wait(sem);

    int x = read_from_shm();
    printf("[Bittu]: Before Subtraction [Result]: %d in Child-%d [CPU]: %d\n", x, getpid(), sched_getcpu());
    printf("a = %d, b = %d\n", a, b);

    int temp = a - b;
    write_to_shm(x + temp);

    int y = read_from_shm();
    printf("[Bittu]: Before Subtraction [Result]: %d in Child-%d [CPU]: %d\n", x, getpid(), sched_getcpu());

    sem_post(sem);

    return 0;
}
