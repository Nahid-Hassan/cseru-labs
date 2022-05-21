#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <string.h>
#include <fcntl.h>
#include <sched.h>
#include <semaphore.h>
#include <sys/wait.h>

#include "rwshem.h"

int main() {
    pid_t cpid;
    int result, x, y;

    printf("Enter the value of x & y: ");
    scanf("%d %d", &x, &y);

    result = 0;
    write_to_shm(result); /* define in rwshem.h */
    
    // named shemaphore is created by sem_open()
    // sem_open() returns a sem_t *
    // sem_open() takes 3 arguments:
    // 1. name of the semaphore
    // 2. flags
    // 3. permissions
    sem_t *sem = sem_open("/sem", O_CREAT, 0666, 1);

    for (int i = 0; i < 3; i++) {
        cpid = fork();
        if (cpid < 0) {
            perror("forking error.\n");
            exit(-1);
        } else if (cpid == 0) {
            char arg1[10], arg2[10];
            sprintf(arg1, "%d", x);    /* convert x to string */
            sprintf(arg2, "%d", y);    /* convert y to string */

            if (i == 0) {
                execlp("./Ittu", arg1, arg2, NULL);
            } else if ( i == 1) {
                execlp("./Bittu", arg1, arg2, NULL);
            } else if (i == 2){
                execlp("./Mittu", arg1, arg2, NULL);
            }
        } else {
            waitpid(cpid, NULL, 0);
            sem_wait(sem);

            int x = read_from_shm();
            printf("[Laltu] - Result: %d, in parent [CPU]: %d\n", x, sched_getcpu());

            sem_post(sem);
        }
    }

    return 0;
}