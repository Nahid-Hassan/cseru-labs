#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sched.h>

int main()
{
    pid_t pid1;
    pid_t pid2;
    int i;

    pid1 = fork();

    if (pid1 == -1)
    {
        perror("Child Process Creation Failed.\n");
        exit(-1);
    }
    else if (pid1 == 0)
    {
        execlp("./Pillow", "Pillow", NULL);
    }
    else if (pid1 > 0)
    {
        pid2 = fork();

        if (pid2 < 0)
        {
            perror("Child Process Creation Failed.\n");
            exit(-2);
        }
        else if (pid2 == 0)
        {
            execlp("./Killow", "Killow", NULL);
        }
        else if (pid2 > 0)
        {
            while (1)
            {
                printf("Process-%u, parent of Pillow-%u and Killow-%u, running at CPU %d\n", getpid(), pid1, pid2, sched_getcpu());
            }
        }
    }
}
