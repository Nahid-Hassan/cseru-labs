#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
    char buffer[50];

    char *pipePath = "./fifoPipe";
    int fd = open(pipePath, O_RDONLY); // read only

    read(fd, buffer, sizeof(buffer));  // read from pipe
    printf("%s\n", buffer);
}
