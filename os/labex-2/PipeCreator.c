#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char const *argv[])
{
    int i;

    for (i = 1; i < argc; i++) {
        // create nammed pipe using mkfifo
        if (mkfifo(argv[i], 0777) == -1) {
            perror("[mkfifo failed]");
            return 1;
        }
    }

    return 0;
}
