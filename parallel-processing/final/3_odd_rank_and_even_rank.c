#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank % 2) printf("I am rank %d, and I am odd rank\n", rank);
    else printf("I am rank %d, and I am even rank\n", rank);

    MPI_Finalize();
    return 0;
}

/*
$ mpicc 3_odd_rank_and_even_rank.c -o odd_even
$ mpirun -np 4 odd_even

I am rank 2, and I am even rank
I am rank 3, and I am odd rank
I am rank 1, and I am odd rank
I am rank 0, and I am even rank
*/