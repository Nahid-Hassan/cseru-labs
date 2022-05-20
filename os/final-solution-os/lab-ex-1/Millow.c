#define  _GNU_SOURCE
#include <stdio.h>     /* printf */
#include <sys/types.h> /* pid_t  */
#include <unistd.h>    /* fork   */
#include <stdlib.h>    /* exit   */
#include <sys/wait.h>  /* wait   */
#include <sched.h>     /* sched_getcpu */
#include <stdbool.h>   /* bool */

int main() {
    /*
     * Millow process create two children. The first child will call the "./Pillow" process and show it's PID and CPU-information and second child will call the "./Killow" process and show it's PID and CPU-information.
    */
    pid_t cpid1, cpid2, pid;
    int cpuId;

    /*
                                        Millow.c (pid, cpid1, cpid2, cpu-info)
                                          /\     
                                         /  \
                                        /    \
                    (pid, cpu-info) Pillow.c  Killow.c (pid, cpu-info)

    */

    cpid1 = fork();

    if (cpid1 < 0) {
        printf("Error[1]: fork() failed\n");
        exit(1);
    } else if (cpid1 == 0) {
        execlp("./Pillow", "Pillow", NULL);
    } else if (cpid1 > 0) {
        cpid2 = fork();

        if (cpid2 < 0) {
            printf("Error[2]: fork() failed\n");
            exit(1);
        } else if (cpid2 == 0) {
            execlp("./Killow", "Killow", NULL);
        } else if (cpid2 > 0) {
            while (true) {
                pid = getpid();
                cpuId = sched_getcpu();

                printf("Process-%u, Parent of Pillow-%u and Killow-%u, CPU-%d\n", pid, cpid1, cpid2, cpuId);
            }
        }
    }

    return 0;
}