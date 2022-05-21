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