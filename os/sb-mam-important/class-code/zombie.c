/**
 * @file zombie.c
 * @author your name (Md. Nahid Hassan)
 * @brief A zombie process is a process that has terminated but is still in the process table.
 * @version 0.1
 * @date 2022-01-08
 *
 * @copyright Copyright (c) 2022
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

int main(int argc, char *argv[]) {
    int pid;
    pid = fork();

    if (pid < 0) {
        perror("fork error\n");
        exit(0);
    } else if (pid == 0) {
        printf("I am the child process and my pid is = %d and my parent pid is = %d\n", getpid(), getppid());
    } else if (pid > 0) {
        /**
         * @brief how zombie process create here?
         * 1. parent process create child process.
         * 2. child process terminate and parent is sleeping.
         * 3. now parent process is waiting for child but child is
         *    already terminate so now child process is zombie process.
         * 4. parent process terminate.
         */
        sleep(20);
        printf("I am the parent process and my pid is = %d and my parent pid is = %d\n", getpid(), getppid());
    }
}
