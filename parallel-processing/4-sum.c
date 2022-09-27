#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv) {
    MPI_Init(&argc, &argv);

    int n = 12;                   // total data point
    int np = 4;                   // total process number
    int rank;                     // for process rank
    int sections = n / (np - 1);  // just for my laptop
    int root_process = 0;         // root process
    int sub_nums[20];

    MPI_Status status;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == root_process) {
        int nums[20] = {1,2,3,4,5,6,7,8,9,10,11,12};

        // send the data
        MPI_Send(nums, sections, MPI_INT, 1, 25, MPI_COMM_WORLD);
        MPI_Send(nums + (sections * 1), sections, MPI_INT, 2, 25, MPI_COMM_WORLD);
        MPI_Send(nums + (sections * 2), sections, MPI_INT, 3, 25, MPI_COMM_WORLD);

        // receive the data
        int total = 0;
        for (int i = 0; i < np - 1; i++) {
            int out;
            MPI_Recv(&out, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
            total += out;
        }
        printf("Total sum: %d\n", total);
    } else {
        MPI_Recv(&sub_nums, sections, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

        int sum = 0;
        for (int i = 0; i < sections; i++) {
            sum += sub_nums[i];
        }
        
        printf("From %i rank: %d is the sum value.\n", rank, sum);
        MPI_Send(&sum, 1, MPI_INT, 0, 25, MPI_COMM_WORLD);
    }

    return 0;
}