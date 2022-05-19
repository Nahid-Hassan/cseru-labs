#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    char *argv[] = {"ls", "-l", NULL};
    /**
     * @brief execlp() is similar to execl(), but it searches for the command in the PATH environment variable.
     * execlp() is a wrapper function for the execvp() function.
     * @param pathname The name of the file to execute.
     * @param argv A pointer to an array of pointers to strings, each of which is an argument to the new program.
     * @return If the function succeeds, it returns a non-negative value.
     * If the function fails, it returns -1.
     * @remark The execvp() function is a wrapper function for the execv() function.
     * The execvp() function is used to execute a program.
     */

    // execvp("ls", argv);
    // we have another source hi.c file, so we can use execlp() to execute it.
    // first we need to compile it.
    // $ gcc -o hi hi.c
    // then we can use execlp() to execute it.

    int pid = fork();

    if (pid < 0) {
        perror("fork error\n");
    } else if (pid == 0) {
        /**
         * @brief execlp(path, arg1, arg2, ....., argN, NULL);
         * path: the name of the file to execute. object file.
         * arg1, arg2, ..., argN: the arguments to the new program.
         * NULL: the end of the argument list.
         */

        execlp("./test","test", NULL);
    } else {
        printf("I am the parent process.\n");
        /**
         * @brief wait() is used to wait for a child process to terminate.
         */
        wait(NULL);
    }


    return 0;
}
