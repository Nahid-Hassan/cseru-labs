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

int main(){
	pid_t cpid;
	int result, sid;

    printf("Enter the value of x & y: ");
    int x, y;
    scanf("%d%d", &x, &y);

	result = 0; // Shared data
	write_to_shm(result);

    // named semaphore is created using sem_open
    sem_t *sem = sem_open("/named_semaphore", O_CREAT, 0666, 1);
    if (sem == SEM_FAILED) {
        printf("Semaphore error\n");
        exit(-1);
    }

	for (int i = 0; i < 3; i++) {
		cpid = fork();

		if (cpid < 0) {
			printf("Child process creation failed.\n");
			exit(0);
		} else if (cpid == 0){
            // n-child process
            char arg1[10], arg2[10];
            sprintf(arg1, "%d", x);
            sprintf(arg2, "%d", y);
			if (i == 0) {
                execlp("./Ittu", arg1, arg2, NULL);
			}
			else if (i == 1) {
				execlp("./Bittu", arg1, arg2, NULL);
			}
            else if (i == 2) {
                execlp("./Mittu", arg1, arg2, NULL);
            }

		} else { 
			waitpid(cpid, NULL, 0);
			sem_wait(sem);

			int x = read_from_shm();
			printf("[Laltu] - Result: %d, in Parent [CPU]: %d\n", x, sched_getcpu());

			sem_post(sem);
		}
	}


	return 0;
}
