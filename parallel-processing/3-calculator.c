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