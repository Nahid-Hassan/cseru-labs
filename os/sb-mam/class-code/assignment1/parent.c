

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int i = 0;

    fork();
    printf("Hi%d\n", ++i);

    fork();
    printf("Hey%d\n", ++i);

    fork();
    printf("Hello%d\n", ++i);

    return 0;
}
