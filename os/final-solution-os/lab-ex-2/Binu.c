#include <stdio.h> /* perror, printf */
#include <stdlib.h> /* exit */
#include <string.h> /* strcat */
#include <unistd.h> /* access, F_OK */
#include <fcntl.h> /* open */

int main(int argc, char const *argv[]) {
    char buffer[100];
    
    while (1) {
        /* !!IMPORTANT - open pipe as READ only */
        int fd = open(argv[1], O_RDONLY);
        read(fd, buffer, 100);
        close(fd);

        printf("%s\n", buffer);
        if(strcmp(buffer, "bye") == 0) {
            /* !!IMPORTANT - open pipe as write only */
            fd = open(argv[1], O_WRONLY);

            /* write message to pipe */
            write(fd, "Binu say bye", strlen("bye") + 1);
            close(fd);
            exit(0);
        }
    }

    return 0;
}