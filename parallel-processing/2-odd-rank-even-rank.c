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