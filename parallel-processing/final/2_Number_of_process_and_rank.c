#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);

    int np;
    int rank;

    // get number of process
    MPI_Comm_size(MPI_COMM_WORLD, &np);
    // get rank
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    printf("I am rank %d and number of process is %d\n", rank, np);

    MPI_Finalize();
    return 0;
}

/**
$ mpicc 2_Number_of_process_and_rank.c -o rank_process
$ mpirun -np 4 rank_process
I am rank 1 and number of process is 4
I am rank 2 and number of process is 4
I am rank 3 and number of process is 4
I am rank 0 and number of process is 4
*/