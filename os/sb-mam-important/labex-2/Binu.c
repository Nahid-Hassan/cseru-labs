#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char const *argv[]) {
    while(1) {
        char buffer[100];

        int fd = open(argv[1], O_RDONLY);

        if (fd < 0)
        {
            printf("File Open Failed\n");
            exit(-1);
        }

        read(fd, buffer, sizeof(buffer));
        printf("[MSG]: %s\n", buffer);

        if (!strcmp(buffer, "Bye")){
            exit(0);
        }
    }

    return 0;
}
