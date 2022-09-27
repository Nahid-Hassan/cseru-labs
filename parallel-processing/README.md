# Parallel Processing 

<http://condor.cc.ku.edu/~grobe/docs/intro-MPI-C.shtml>

**Table of Contents**:

- [Parallel Processing](#parallel-processing)
  - [Setup](#setup)
  - [Lab - 1 (Setup System - 2022-06-23)](#lab---1-setup-system---2022-06-23)
  - [MPI Programming Basic Structure](#mpi-programming-basic-structure)
  - [MPI Hello World](#mpi-hello-world)
  - [Identifying the separate processes](#identifying-the-separate-processes)
  - [Lab Experiment - 1 (Number or Process and Rank)](#lab-experiment---1-number-or-process-and-rank)
  - [Experiment-2 (Odd and Even Ranked Process)](#experiment-2-odd-and-even-ranked-process)
  - [Experiment - 3 (MPI Calculator)](#experiment---3-mpi-calculator)
  - [Understand Message Passing](#understand-message-passing)
  - [Bernstain Algorithm](#bernstain-algorithm)

## Setup

**Install `openmpi`**:

```bash
nahid@cseru:~$ sudo apt install openmpi-bin openmpi-common openmpi-doc libopenmpi-dev

nahid@cseru:~$ mpicc --version
gcc (Ubuntu 11.2.0-19ubuntu1) 11.2.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

nahid@cseru:~$ mpirun --version
mpirun (Open MPI) 4.1.2

Report bugs to http://www.open-mpi.org/community/help/
nahid@cseru:~$ 

```

## Lab - 1 (Setup System - 2022-06-23)

**To know total CPU-cores information**:

```bash
nahid@cseru $ grep -c processor /proc/cpuinfo
4                                                   # for my case it is 4
```

**Hello World**:

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

## Understand Message Passing

## Bernstain Algorithm

`in.txt`

```txt
P1: C:=D*E;
P2: M:=G+C;
P3: A:=B+C;
P4: C:=L+M;
P5: F:=G/E;
```

`./bernstain.cpp`

```c++
#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("in.txt", "r", stdin);

    vector<vector<char>> in;
    vector<char> out;
    string s;


    while(getline(cin, s)) {
        bool flag = true;
        vector <char> temp;
        for (long unsigned int i = 1; i < s.size(); i++) {
            if (flag && isalpha(s[i])) {
                out.push_back(s[i]);
                flag = false;
                continue;
            }
            if (!flag && isalpha(s[i])) {
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }
    
    for (long unsigned int i = 0; i < in.size(); i++) {
        for (long unsigned int j = i + 1; j < in.size(); j++) {
            if (find(in[i].begin(), in[i].end(), out[j]) != in[i].end()) {
                cout << "P" << i + 1 << " and P" << j + 1 << " are anti-independent.\n";
                continue;
            }
            if (find(in[j].begin(), in[j].end(), out[i]) != in[j].end()) {
                cout << "P" << i + 1 << " and P" << j + 1 << " are follow-dependent.\n";
                continue;
            }
            if (out[i] == out[j]) {
                cout << "P" << i + 1 << " and P" << j + 1 << " are output-dependent.\n";
                continue;
            }
            cout << "P" << i + 1 << " and P" << j + 1 << " are parallel.\n";
        }
    }
}
```

```bash
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing/bernstain$ g++ bernstain.cpp 
nahid@cseru:/media/nahid/data-center/workspace/cseru-labs/parallel-processing/bernstain$ ./a.out 
P1 and P2 are follow-dependent.
P1 and P3 are follow-dependent.
P1 and P4 are output-dependent.
P1 and P5 are parallel.
P2 and P3 are parallel.
P2 and P4 are anti-independent.
P2 and P5 are parallel.
P3 and P4 are anti-independent.
P3 and P5 are parallel.
P4 and P5 are parallel.
```