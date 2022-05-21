### Lab Experiment - 3

```
Create a process, named MultiHead, having three threads, named Ittu, Bittu, and Mittu .

- Ittu, Bittu, and Mittu  perform addition, subtraction and multiplication of two variables 
  sent by the main thread of the process and keep the output in a global variable, result. 
  All threads print their process ID, thread ID, CPU Info and 

- the global variable, 'result'.
- The main thread waits until each thread finish its task.
- The main thread reads and sends two integer values to each thread 100 times.
- If any thread finds that 'result' = 100, it immediately send signal to the main thread to stop the process.


** Take necessary steps to avoid thread racing.
```

**Understand Problem**: Under `MultiHead` there are three thread name Ittu, Bittu and Mittu. All the thread show there pid, thread_id and cpu-inforamtion. There is a global variable name `result`. In main thread we take two integer numbers and run every thread 100 times and perform 

- Ittu(Addition)
- Bittu(Subtraction)
- Mittu(Multiplication)

on the global variable `result`. If any time result == 10, the thread send a signal using `pthread_kill()`


**Files**:

`./MultiHead.c`

**Explain**:

1. **Create thread**:

```c
    pthread_t Ittu, Bittu, Mittu;

    /* read two  integer number */
    scanf("%d %d", &nums[0], &nums[1]);
    
    for (int i = 0; i < 100; i++){
        pthread_create(&Ittu, NULL, addition, (void *)&nums);
        pthread_create(&Bittu, NULL, subtraction, (void *)&nums);
        pthread_create(&Mittu, NULL, multiplication, (void *)&nums);

        printf("\n\n");

        sleep(.1);
    }

    // Ittu, Bittu, and Mittu  join the main thread of the process.
    pthread_join(Ittu, NULL);
    pthread_join(Bittu, NULL);
    pthread_join(Mittu, NULL);
```

Here,

- `pthread_t Ittu, Bittu, and Mittu` is the **thread name**.
- Using `pthread_create()` we can create a thread.
- `pthread_create()` take four parameters. 
    
    1. `Thread name` that we create using `pthread_t`.
    2. `Attribute`. For our case it is NULL.
    3. `Service routine or function.`
    4. `Argument` as `void *arg`
- `pthread_join()` — Wait for a thread to **end**.


**Explanation of one service routine or method or function**: 

- `mutex` is a pthread_mutex_t type global variable. That we used in mutex_lock to avoid **thread_racing** 

```c
pthread_mutex_t mutex;       
```

```c
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
    return NULL;
}
```

- In the method at the beginning and ending we add 

```c
    pthread_mutex_lock(&mutex);

    // define you service routine job

    pthread_mutex_unlock(&mutex);
```

- `pthread_kill(pthread_self(), SIGUSR1)`

The  pthread_kill() function sends the signal sig to thread, a thread in the same process as the caller.  The signal is asynchronously directed to thread.


> The mutex object referenced by mutex is locked by calling pthread_mutex_lock(). If the mutex is already locked, the calling thread blocks until the mutex becomes available. This operation returns with the mutex object referenced by mutex in the locked state with the calling thread as its owner.



**Compile with -pthread option if show any error while compiling.**:

```bash
$ gcc MultiHead.c -o MultiHead -pthread

$ ./MultiHead
10 20

From addition thread
--------------------
[ADDITION]: Process ID: 14757
[ADDITION]: Thread ID: 139834620368448
[ADDITION]: CPU Info: 0

[ADDITION RESULT] Result: 30

.................
..................
```