#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    int a = 10;
    int b = 5;
    if (rank == 0) printf ("Sum %d + %d = %d\n", a, b, a+b); 
    else if (rank == 1) printf ("Sub %d - %d = %d\n", a, b, a-b); 
    else if (rank == 2) printf ("Mul %d * %d = %d\n", a, b, a*b); 
    else if (rank == 3) printf ("Div %d / %d = %d\n", a, b, a/b); 

    MPI_Finalize();
    return 0;
}

/*
Output:

Mul 10 * 5 = 50
Sum 10 + 5 = 15
Div 10 / 5 = 2
Sub 10 - 5 = 5
*/