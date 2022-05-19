#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main()
{
    // int status;

    // for create pipe, if pipe already exist then it will return -1
    // mkfifo(path, permissions);
    // status = mkfifo("./fifoPipe", 0666);
    // if (status == -1) {
    //     perror("mkfifo"); // mkfifo: File exists
    //     exit(-1);
    // }

    int fd;
    char *pipePath = "./fifoPipe";
    char *msg = "Hello World\n\0";

    fd = open(pipePath, O_WRONLY);
    write(fd, msg, strlen(msg));
    close(fd);
}
