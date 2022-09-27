# Lab-1 Documentation

- [Lab-1 Documentation](#lab-1-documentation)
  - [MPI Programming Basic Structure](#mpi-programming-basic-structure)
  - [MPI Hello World](#mpi-hello-world)
  - [Identifying the separate processes](#identifying-the-separate-processes)
  - [Lab Experiment - 1 (Number or Process and Rank)](#lab-experiment---1-number-or-process-and-rank)
  - [Experiment-2 (Odd and Even Ranked Process)](#experiment-2-odd-and-even-ranked-process)
  - [Experiment - 3 (MPI Calculator)](#experiment---3-mpi-calculator)
  - [Try to understand MPI Communication or Message Passing System](#try-to-understand-mpi-communication-or-message-passing-system)

## MPI Programming Basic Structure

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {
    /* initialize */
    MPI_Init(&argc, &argv);

    /**
     *  write your code here.....
     */

    /* finalize */
    MPI_Finalize();
}
```

When the program starts, it consists of only one process, sometimes called the "parent", "root", or "master" process. When the routine `MPI_Init` executes within the root process, it causes the creation of `3` additional processes (to reach the `number of processes` (np) specified on the `mpirun` command line), sometimes called `"child"` processes.

Each of the processes then continues executing separate versions of the hello world program. The next statement in every program is the printf statement, and each process prints "Hello world" as directed. Since terminal output from every program will be directed to the same terminal, we see four lines saying "Hello world".

## MPI Hello World

`./MPI_Hello_world.c`	

```c++
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) 
{
    MPI_Init(&argc, &argv);
    printf("Hello world\n"); 
       
    MPI_Finalize();
}
```

**Compile & Run the program**:

```bash
nahid@cseru $ mpicc hello_world_mpi.c -o hello
nahid@cseru $ mpirun --use-hwthread-cpus -np 4 ./hello       # -np stands for number of processors
Hello world
Hello world
Hello world
Hello world
```

## Identifying the separate processes

As written, we cannot tell which "Hello world" line was printed by which process. To identify a process we need some sort of `process ID` and a routine that lets a process find its own process ID. MPI assigns an integer to each process beginning with `0` for the **parent process** and incrementing each time a new process is created. A process ID is also called its `"rank"`.

MPI also provides routines that let the process determine its process ID, as well as the number of processes that are have been created.

## Lab Experiment - 1 (Number or Process and Rank)

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
    int rank;       /* also know as process id */
    int np;         /* stand for number of process */

    // "mpirun -np 4 a.out" - agrv contains all informations
    // Initialize the MPI
    MPI_Init(&argc, &argv);


    // Read the function name as,
    // MPI Communication world rank (..., &...);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);  /* pass by reference */
    MPI_Comm_size(MPI_COMM_WORLD, &np);     /* number of process */

    printf("Hello Genius! I am process %i out of process %i processes.\n", rank, np);  

    // Finalize the MPI
    MPI_Finalize();
}
```

```bash
# Compile
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing$ mpicc 1-number-of-process-and-rank.c 

# Execute
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing$ mpirun -np 4 a.out 
Hello Genius! I am process 1 out of process 4 processes.
Hello Genius! I am process 2 out of process 4 processes.
Hello Genius! I am process 3 out of process 4 processes.
Hello Genius! I am process 0 out of process 4 processes.
```

## Experiment-2 (Odd and Even Ranked Process)

```c
/* Write a program in MPI where even ranked process print Hello
   and odd ranked process print World.
*/

#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank % 2) printf("Process Rank - %i, World.\n", rank);
    else printf("Process Rank - %i, Hello.\n", rank);

    MPI_Finalize();
}
```

```bash
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing$ mpicc 2-odd-rank-even-rank.c 
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing$ mpirun -np 4 a.out 
Process Rank - 1, World.
Process Rank - 2, Hello.
Process Rank - 0, Hello.
Process Rank - 3, World.
```

## Experiment - 3 (MPI Calculator)

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {
    int a = 20, b = 10;            // make simple, later i am trying to modify this program
    // scanf("%d%d", &a, &b);
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) printf("Rank - %i, Sum = %d + %d = %d\n", rank, a, b, a + b);
    else if (rank == 1) printf("Rank - %i, Sub = %d - %d = %d\n", rank, a, b, a - b);
    else if (rank == 2) printf("Rank - %i, Mul = %d * %d = %d\n", rank, a, b, a * b);
    else if (rank == 3) {
        if (b != 0) {
            printf("Rank - %i, Div = %d / %d = %d\n", rank, a, b, a / b);
        } else {
            printf("Rank - %i, Cannot divided by zero.\n", rank);
        }
    }

    MPI_Finalize();
}
```

```bash
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing$ mpicc 3-calculator.c 
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing$ mpirun -np 4 a.out 
Rank - 2, Mul = 20 * 10 = 200
Rank - 3, Div = 20 / 10 = 2
Rank - 0, Sum = 20 + 10 = 30
Rank - 1, Sub = 20 - 10 = 10
```

## Try to understand MPI Communication or Message Passing System

