#include <stdio.h> /* printf() */
#include <unistd.h> /* getpid(void), pid_t, fork(void) */
#include <stdlib.h> /* exit(int) */

int main() {
    pid_t pid, cpid, cpid1; /* autoclass storage variable initially take grabage */

    // printf("%d %d %d\n", pid, cpid, cpid1);

    cpid = fork(); /* return 0(success) or -1/-ve(fail) or +ve(child pid pass to parent) */

    if (cpid < 0) {    /* process cannot be negative */
        printf("Unsuccessful\n");
        exit(-1);
    } else if (cpid == 0) {   /* child process */
        cpid1 = getpid();  /* child pid */
        printf("\nI am the child process and my pid = %d\n", cpid1);
    } else if (cpid > 0) {    /* parent process */
        pid = getpid();
        printf("\nI am the parent process and my pid = %d and my child process pid = %d\n", pid, cpid);
    }
}

/**
 * @brief fork()
 *
 * fork() return -1 if it failed to create child process.
 * fork() return 0(to identify child process itself) and it pass to child process.
 * fork() return +ve(child process pid) and it pass to parent process.
 */
