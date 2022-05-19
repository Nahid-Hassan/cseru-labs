#include <stdio.h>
#include <unistd.h>

int count = 0;

int main()
{
    fork();
    fork();
    fork();

    ++count;
    printf("Hello Forking() -  %d\n", count); /* ???what is the output ??? */
}
