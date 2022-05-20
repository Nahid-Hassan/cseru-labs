### Lab Experiment - 3

```
Create a process, named MultiHead, having three threads, named Ittu, Bittu, and Mittu .

- Ittu, Bittu, and Mittu  perform addition, subtraction and multiplication of two variables sent by the main thread of the process and keep the output in a global variable, result. All threads print their process ID, thread ID, CPU Info and 
- the global variable, 'result'.
- The main thread waits until each thread finish its task.
- The main thread reads and sends two integer values to each thread 100 times.
- If any thread finds that 'result' = 100, it immediately send signal to the main thread to stop the process.
Take necessary steps to avoid thread racing.
```

**Compile with -pthread option if show any error while compiling.**:

```bash
$ gcc MultiHead.c -o MultiHead -pthread
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/os/final-solution-os/lab-ex-3$ ./MultiHead
40 60

From addition thread
--------------------
[ADDITION]: Process ID: 7220
[ADDITION]: Thread ID: 140200786839104


[ADDITION]: CPU Info: 2

[ADDITION RESULT] Result: 100
User defined signal 1
```