#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <sched.h>

#define MAX_CPU_COUNT 4
cpu_set_t cpuset;

void *thread_func1()
{
    // show process PID
    printf("[BlackHole-Thread-1]: Child process PID: %d, Parent Process PID %d\n", getpid(), getppid());
    // show logical CPU info
    printf("[BlackHole-Thread-1]: Logical CPU info: %d\n", sched_getcpu());
    // show scheduling algorithm's information
    // if sched_getscheduler(getpid()) == SCHED_FIFO return 0 then RR else FIFO
    printf("[BlackHole-Thread-1]: Scheduling algorithm: %s\n", sched_getscheduler(getpid()) == SCHED_FIFO ? "FIFO" : "RR");
    printf("\n\n");
    return NULL;
}

void *thread_func2()
{
    // show process PID
    printf("[BlackHole-Thread-2]: Child process PID: %d, Parent Process PID %d\n", getpid(), getppid());
    // show logical CPU info
    printf("[BlackHole-Thread-2]: Logical CPU info: %d\n", sched_getcpu());
    // show scheduling algorithm's information
    // if sched_getscheduler(getpid()) == SCHED_FIFO return 0 then RR else FIFO
    printf("[BlackHole-Thread-2]: Scheduling algorithm: %s\n", sched_getscheduler(getpid()) == SCHED_FIFO ? "FIFO" : "RR");
    printf("\n\n");
    return NULL;
}

int main(int argc, char const *argv[])
{
    pthread_t X, Y;

    for (int i = 0; i < 10; i++)
    {
        pthread_create(&X, NULL, thread_func1, NULL);
        pthread_create(&Y, NULL, thread_func2, NULL);

        CPU_ZERO(&cpuset);
        CPU_SET(i % MAX_CPU_COUNT, &cpuset);
        sched_setaffinity(0, sizeof(cpu_set_t), &cpuset);
        printf("\n");
    }

    pthread_join(X, NULL);
    pthread_join(Y, NULL);

    printf("[BlackHole]: Main completed. Exiting.\n");
    
    return 0;
}
