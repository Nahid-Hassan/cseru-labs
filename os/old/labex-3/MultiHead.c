#define _GNU_SOURCE
#define _POSIX_SOURCE

#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>
#include <sched.h>
#include <time.h>
#include <signal.h>

int result = 0;
int nums[2] = {0, 0};
pthread_mutex_t mutex;


void *addition(void *args)
{
    pthread_mutex_lock(&mutex);
    printf("\nFrom addition thread\n--------------------\n");
    // All threads print their process ID, thread ID, CPU Info and the Result, 'result'.
    printf("[ADDITION]: Process ID: %d\n", getpid());
    printf("[ADDITION]: Thread ID: %ld\n", pthread_self());
    printf("[ADDITION]: CPU Info: %d\n", sched_getcpu());

    int *x = args;
    result = x[0] + x[1];

    printf("\n[ADDITION RESULT] Result: %d\n", result);

    // send signal to main thread if result is 100
    if (result == 100) {
        pthread_kill(pthread_self(), SIGUSR1);
    }
    pthread_mutex_unlock(&mutex);
}

void *subtraction(void *args) {
    pthread_mutex_lock(&mutex);
    printf("\nFrom subtraction thread\n--------------------\n");

    // All threads print their process ID, thread ID, CPU Info and the Result, 'result'.
    printf("[SUBTRACTION]: Process ID: %d\n", getpid());
    printf("[SUBTRACTION]: Thread ID: %ld\n", pthread_self());
    printf("[SUBTRACTION]: CPU Info: %d\n", sched_getcpu());

    int *x = args;
    result = x[0] - x[1];

    printf("\n[SUBTRACTION RESULT] Result: %d\n", result);

    // send signal to main thread if result is 100
    if (result == 100)
    {
        pthread_kill(pthread_self(), SIGUSR1);
    }
    pthread_mutex_unlock(&mutex);
}

void *multiplication(void *args) {
    pthread_mutex_lock(&mutex);
    printf("\nFrom multiplication thread\n--------------------\n");
    printf("[MULTIPLICATION]: Process ID: %d\n", getpid());
    printf("[MULTIPLICATION]: Thread ID: %ld\n", pthread_self());
    printf("[MULTIPLICATION]: CPU Info: %d\n", sched_getcpu());

    int *x = args;
    result = x[0] * x[1];

    printf("\n[MULTIPLICATION RESULT]: Result: %d\n", result);

    // send signal to main thread if result is 100
    if (result == 100)
    {
        pthread_kill(pthread_self(), SIGUSR1);
    }
    pthread_mutex_unlock(&mutex);
}

int main(int argc, char const *argv[])
{
    // create 3 threads name Ittu, Bittu, and Mittu
    pthread_t Ittu, Bittu, Mittu;

    /* read two  integer number */
    scanf("%d %d", &nums[0], &nums[1]);
    
    for (int i = 0; i < 100; i++){
        pthread_create(&Ittu, NULL, addition, (void *)&nums);
        pthread_create(&Bittu, NULL, subtraction, (void *)&nums);
        pthread_create(&Mittu, NULL, multiplication, (void *)&nums);

        printf("\n\n");
        // sleep(.1);
    }

    // Ittu, Bittu, and Mittu  join the main thread of the process.
    pthread_join(Ittu, NULL);
    pthread_join(Bittu, NULL);
    pthread_join(Mittu, NULL);

    return 0;
}
