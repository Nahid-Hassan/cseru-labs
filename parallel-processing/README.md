# Parallel Processing 

<http://condor.cc.ku.edu/~grobe/docs/intro-MPI-C.shtml>

**Table of Contents**:

- [Parallel Processing](#parallel-processing)
	- [Setup](#setup)
	- [Lab - 1 (Setup System - )](#lab---1-setup-system---)

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

`./hello_world_mpi.c`	

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

