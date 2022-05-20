#include <stdio.h> /* perror, printf */
#include <unistd.h> /* access, F_OK */
#include <sys/stat.h> /* mkfifo */

int main(int argc, char const *argv[]) {
    // argv[0] = ./PipeCreator
    // argv[1] = pipe1 
    // argv[2] = pipe2

    for (int i = 1; i < argc; i++) {
        /* check if file exists */
        if (access(argv[i], F_OK) == 0) {
            printf("Pipe %s already exists.\n", argv[i]);
            continue; /* if file is already exits continue to next iteration.*/
        }

        if (mkfifo(argv[i], 0777) == -1) {
            perror("[mkfifo] - PipeCreation failed.\n");
        } else {
            printf("[mkfifo] - Pipe %s created.\n", argv[i]);
        }
    }

    return 0;
}
