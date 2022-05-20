#include <stdio.h> /* perror, printf, sprintf */
#include <string.h> /* strcat */
#include <unistd.h> /* access, F_OK */
#include <stdlib.h> /* exit */
#include <fcntl.h> /* open */

int main(int argc, char const *argv[]) {
    char msg[100];    /* message to be sent */ 
    char cpid[10];    /* to store child pid */
    char ppid[10];    /* to store parent pid */
    
    /* convert int to string */
    sprintf(cpid, "%d", getpid());
    sprintf(ppid, "%d", getppid());

    /* create message */
    /* Hello, child pid is <cpid> and parent pid is <ppid>!*/
    strcat(msg, "Hello, child pid - ");
    strcat(msg, cpid);
    strcat(msg, " from Parent pid - ");
    strcat(msg, ppid);
    strcat(msg, "!");

    /* open pipe */
    int fd = open(argv[1], O_WRONLY);
    if (fd == -1) {
        perror("[open] - Pipe opening failed.\n");
        return 1;
    }

    /* write message to pipe */
    write(fd, msg, strlen(msg) + 1);
    close(fd);

    while(1) {
        fd = open(argv[1], O_WRONLY);
        char buffer[100];
        scanf("%s", buffer);
        write(fd, buffer, strlen(buffer) + 1);
        close(fd);

        if (strcmp(buffer, "bye") == 0) {
            fd = open(argv[1], O_RDONLY);
            read(fd, buffer, 100);
            close(fd);
            printf("%s\n", buffer);
            exit(0);
        }
    }

    return 0;
}