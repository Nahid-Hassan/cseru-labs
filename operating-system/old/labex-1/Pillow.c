#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sched.h>

int main(int argc, char const *argv[]) {

    while(1) {
        printf("I am child-%d running at CPU-%d.\n", getpid(), sched_getcpu());
    }

    return 0;
}
