#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    // msg for initial sending
    char msg[100];

    char cPid[100];
    char pPid[100];

    // convert int to string
    sprintf(cPid, "%d", getpid());
    sprintf(pPid, "%d", getppid());

    // generate first massage
    strcat(msg, "Hello ");
    strcat(msg, ",Child Pid - ");
    strcat(msg, cPid);
    strcat(msg, ",Parent - ");
    strcat(msg, pPid);

    int fd = open(argv[1], O_WRONLY);
    if (fd < 0) {
        printf("Failed to open pipe.\n");
        exit(-1);
    }

    write(fd, msg, strlen(msg) + 1);

    while (1)
    {
        char buffer[100];
        fd = open(argv[1], O_WRONLY);
        if (fd < 0) {
            printf("Failed to open pipe.\n");
            exit(-1);
        }
        scanf("%s", buffer);
        write(fd, buffer, strlen(buffer) + 1);
        if (!strcmp(buffer, "Bye")) {
            exit(0);
        }
    }

    close(fd);

    return 0;
}
