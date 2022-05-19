#define  _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sched.h>

int main() {
    pid_t cpid1, cpid2, pid;
    int cpuID;
    int i;

    cpid1 = fork();
    if (cpid1 < 0) { // negative value for failure
        printf("Child process creating unsuccessful\n");
        exit(-1); // turn off execution
    }
    else if (cpid1 == 0) { // '0' for child process and start child process
        for (i = 0; i < 1; i--) {
            pid = getpid();
            cpuID = sched_getcpu();
            printf("I am child1 %u running at CPU-%d\n", pid, cpuID);
        }
    }
    else if (cpid1 > 0) { // > 0 for parent process and start parent process
        cpid2 = fork();
        if (cpid2 < 0) { // negative value for failure
            printf("Child process creating unsuccessful\n");
            exit(-1); // turn off execution
        }
        else if (cpid2 == 0) { // '0' for child process and start child process
            for (i = 0; i < 1; i--) {
                pid = getpid();
                cpuID = sched_getcpu();
                printf("I am child2 %u running at CPU-%d\n", pid, cpuID);
            }
        }
        else if (cpid2 > 0) { // > 0 for parent process and start parent process
            for (i = 0; i < 1; i--) {
                pid = getpid();
                cpuID = sched_getcpu();
                printf("Process-%u, parent of Pillow-%u and Killow-%u, running at CPU %d\n", pid, cpid1, cpid2, cpuID);
            }
        }
    }



    return 0;
}
