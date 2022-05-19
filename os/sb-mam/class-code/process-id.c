#include <stdio.h>
#include <unistd.h> /* getpid, pid_t, getppid */

int main() {
    // __pid_t pid;    /* __pid_t only used in debian based Operating System */

    /* pid_t is actually is the typedef of the __pid_t */
    /* #typedef __pid_t pid_t */

    pid_t pid; /* to store current process process id */
    pid_t ppid; /* to store current process parent process id */


    /* signature: pid_t getpid(void) and pid_t getppid(void) */
    pid = getpid(); /* return current process process id */
    ppid = getppid(); /* return current process parent process id */

    printf("Current process pid: %d\n", pid);
    printf("Current process parent's pid: %d\n", ppid);

    while(1)
        ;
}

/**
 * @brief
 *
 * The pid_t data type is a signed integer type which is capable of representing a process ID.
 * In the GNU C Library, this is an int. The getpid function returns the process ID of the current process.
 *
 * Source: https://www.gnu.org/software/libc/manual/html_node/Process-Identification.html
 */
