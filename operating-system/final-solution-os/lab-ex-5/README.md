### Lab Experiment - 5


**Question**:

```
- Create a process named, Galaxy, having two child processes, named Nebula and BlackHole.


                                      Galaxy.c (wait for Nebula and BlackHole)
                                          /\     
                                         /  \
                                        /    \
                    (X, Y Threads) Nebula.c  BlackHole.c (X, Y Threads)
                    [100 times in loop]       [100 times in loop] 
                    
                    [PID, CPU-INFO, CPU_Affinity, Scheduling Algo]     -> All three process.

- Nebula and BlackHole are in 100 times loop.
- Main threads of all processes are in 10 times loop.
- Galaxy waits for Nebula and Blackhole to be finished.
- Both Nebula and BlackHole have  two threads, named X and Y.
- All threads of Galaxy, Nebula and BlackHole show their PID, logical CPU info, CPU_Affinity and 
  scheduling algorithm's information.

- Check whether any threads and any processes change their logical processors during their execution.
- Force Blackhole's all threads run in different logical processors whenever they are in the running state.
- Force Nebula to use a scheduling algorithm other than default scheduling algorithm.
```

**Solution**:

- `./Galaxy.c`        # Main process -> run both `Nebula` and `BlackHole` process. 
- `./Nebula.c`     
- `./BlackHole.c`

**Compile and Run**

```bash
$ gcc Galaxy.c -o Galaxy
$ gcc Nebula.c -o Nebula
$ gcc BlackHole.c -o BlackHole

$ ./Galaxy

[BlackHole-Thread-2]: Child process PID: 11661, Parent Process PID 11659
[BlackHole-Thread-2]: Logical CPU info: 2
[BlackHole-Thread-2]: Scheduling algorithm: RR


[Nebula-Thread-2]: Child process PID: 11660, Parent Process PID 11659
[Nebula-Thread-2]: Logical CPU info: 3
[Nebula-Thread-2]: Scheduling algorithm: RR


[Nebula-Thread-1]: Child process PID: 11660, Parent Process PID 11659
[Nebula-Thread-1]: Logical CPU info: 3
[Nebula-Thread-1]: Scheduling algorithm: RR


[BlackHole-Thread-2]: Child process PID: 11661, Parent Process PID 11659
[Nebula-Thread-1]: Child process PID: 11660, Parent Process PID 11659
[Nebula-Thread-1]: Logical CPU info: 1
[BlackHole-Thread-2]: Child process PID: 11661, Parent Process PID 11659
[BlackHole-Thread-2]: Logical CPU info: 0
[BlackHole-Thread-2]: Scheduling algorithm: RR


[Nebula-Thread-1]: Child process PID: 11660, Parent Process PID 11659
[Nebula-Thread-1]: Logical CPU info: 0
[Nebula-Thread-1]: Scheduling algorithm: RR

[Nebula]: Main completed. Exiting.
[BlackHole-Thread-1]: Child process PID: 11661, Parent Process PID 11659
[BlackHole-Thread-1]: Logical CPU info: 0
[BlackHole-Thread-1]: Scheduling algorithm: RR


[MAIN]: Child process PID: 11659, Parent Process PID 9856
[MAIN]: Logical CPU info: 0
[MAIN]: Scheduling algorithm: RR
```

You can see, Here always showing Scheduling algorithm is **RR**. !!!!!!!!! What !!!!!!!!!!!!

**To change scheduling algorithm we need run our ./Galaxy program as a super user.**:

```
$ sudo ./Galaxy

[Nebula-Thread-2]: Child process PID: 11847, Parent Process PID 11846
[Nebula-Thread-2]: Logical CPU info: 0
[Nebula-Thread-2]: Scheduling algorithm: FIFO


[Nebula-Thread-1]: Child process PID: 11847, Parent Process PID 11846
[Nebula-Thread-1]: Logical CPU info: 0
[Nebula-Thread-1]: Scheduling algorithm: FIFO


[BlackHole-Thread-2]: Child process PID: 11848, Parent Process PID 11846
[BlackHole-Thread-2]: Logical CPU info: 3
[BlackHole-Thread-2]: Scheduling algorithm: RR
[Nebula]: Main completed. Exiting.



[BlackHole-Thread-2]: Child process PID: 11848, Parent Process PID 11846
[BlackHole-Thread-2]: Logical CPU info: 0
[BlackHole-Thread-2]: Scheduling algorithm: RR
```

Now both **RR** and **FIFO** scheduling algorithm is used.


**Constraints**:

- `Galaxy` main process run 10 times.
- `Nebula` and `BlackHole` run 100 times from the `Galaxy` process using `execlp()`.
- Both `Nebula` and `BlackHole` have two `X` and `Y` threads and runtime it change its CPU and Scheduling algorithm.


**Task**:

```c
            for (i = 0; i < 10; i++)
            {
                /* Clears set, so that it contains no CPUs. */
                CPU_ZERO(&cpuset);
                /* Add Cpu to set, i % MAX_CPU_COUNT is randomize the cpu set*/
                /* MAX_CPU_COUNT contains value 4 */
                CPU_SET(i % MAX_CPU_COUNT, &cpuset);
                
                /* set the process affinity */
                sched_setaffinity(0, sizeof(cpu_set_t), &cpuset);

                struct sched_param sp = {.sched_priority = 80};
                sched_setscheduler(0, SCHED_FIFO, &sp);

                // show process PID
                printf("[MAIN]: Child process PID: %d, Parent Process PID %d\n", getpid(), getppid());
                // show logical CPU info
                printf("[MAIN]: Logical CPU info: %d\n", sched_getcpu());
                // show scheduling algorithm's information
                printf("[MAIN]: Scheduling algorithm: %s\n", sched_getscheduler(getpid()) == SCHED_FIFO ? "FIFO" : "RR");
            }
```

1. **Change CPU**:

```c
    /* Clears set, so that it contains no CPUs. */
    CPU_ZERO(&cpuset);
    /* Add Cpu to set */
    CPU_SET(i % MAX_CPU_COUNT, &cpuset);            
```

- `cpu_set_t cpuset;` a global variable.
- `CPU_ZERO(&cpuset)` -> clear the set, so that it contains no CPUs.
- CPU_SET(0-3, &cpuset); -> For my system total CPU no is 4. So the first parameter must be in `0 to 3`. 

```c
CPU_SET(2, &cpuset);  // set cpu no 2 for this process.
```

2. **Change CPU-Affinity**:

```c
    /* set the process affinity */
    sched_setaffinity(0, sizeof(cpu_set_t), &cpuset);
```

3. **Change Scheduling Algorithm**:

```c
    struct sched_param sp = {.sched_priority = 80};
    sched_setscheduler(0, SCHED_FIFO, &sp);
```

- `sched_setscheduler()` take 3 arguments `0`, `SCHEDULING_ALGORITHM`, `sched_param` structure 
  that contains `sched_priority`

4. **Final - Showing the which scheduling algorithm is used**:

```c
    // if sched_getscheduler(getpid()) == SCHED_FIFO return 0 then RR else FIFO
    sched_getscheduler(getpid()) == SCHED_FIFO ? "FIFO" : "RR"
```

- Default scheduling algorithm is RR. That's why `sched_getscheduler(getpid())` return 0 naturally. If our forcefully scheduling algorithm make change in scheduling algorithm it returns 1 and 1 == 1 return 1 and print `FIFO`.

