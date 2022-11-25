#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);

    printf("Hello world\n");

    MPI_Finalize();
    return 0;
}

/**
 * Compile: $ mpicc 1_MPI_Hello_world.c -o hello
 * Run    : $ mpirun -np 4 ./hello
 * 
 * Output:
 * Hello World
 * Hello World
 * Hello World
 * Hello World
*/