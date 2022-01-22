#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sched.h>

#define LOOP_CONTROL 100
#define MAX_CPU_COUNT 4
cpu_set_t cpuset;

int main(int argc, char const *argv[])
{
    int i;
    pid_t pid, pid1;
    pid = fork();


    if (pid < 0) {
        perror("Child process creation failed");
        exit(1);
    } else if (pid == 0) {
        /* Nebula Process */
        for(i = 0; i < LOOP_CONTROL; i++) {
            execlp("./Nebula", "Nebula", NULL);
            printf("\n\n");
        }
    } else if (pid > 0) {
        pid1 = fork();
        if (pid1 < 0) {
            perror("Child process creation failed");
            exit(1);
        } else if (pid1 == 0) {
            /* Black Hole Process */
            for(i = 0; i < LOOP_CONTROL; i++) {
                printf("\n\n%d\n",i);
                execlp("./BlackHole", "BlackHole", NULL);
                printf("\n\n");
            }
        } else if(pid1 > 0) {
            wait(NULL);

            for (i = 0; i < 10; i++)
            {
                CPU_ZERO(&cpuset);
                CPU_SET(i % MAX_CPU_COUNT, &cpuset);
                sched_setaffinity(0, sizeof(cpu_set_t), &cpuset);

                struct sched_param sp = {.sched_priority = 80};
                int ret = sched_setscheduler(0, SCHED_FIFO, &sp);

                // show process PID
                printf("[MAIN]: Child process PID: %d, Parent Process PID %d\n", getpid(), getppid());
                // show logical CPU info
                printf("[MAIN]: Logical CPU info: %d\n", sched_getcpu());
                // show scheduling algorithm's information
                printf("[MAIN]: Scheduling algorithm: %s\n", sched_getscheduler(getpid()) == SCHED_FIFO ? "FIFO" : "RR");
            }
        }
    }



    return 0;
}
