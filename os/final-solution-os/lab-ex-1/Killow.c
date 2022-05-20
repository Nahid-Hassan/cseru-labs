#define  _GNU_SOURCE
#include <stdio.h>     /* printf */
#include <sched.h>     /* sched_getcpu */
#include <stdbool.h>   /* bool */
#include <sys/types.h> /* pid_t  */
#include <unistd.h>    /* fork   */


int main() {
    while(true) {
        printf("I am child-%u running at %u.\n", getpid(), sched_getcpu());
    }

    return 0;
}