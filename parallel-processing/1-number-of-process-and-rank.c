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