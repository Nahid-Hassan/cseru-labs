#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    // printf("I from another source file.\n");
    // printf("%d\n", argc);

    // if (argc >= 1)
    // {
    //     printf("%s\n", argv[0]);
    //     printf("%s\n", argv[1]);
    // }

    int i;
    int count = 0;
    for(i = 0; i < 4; i++)
    {
        fork();
    }
    printf("I am the parent. %d\n", i);

    exit(0);
}
