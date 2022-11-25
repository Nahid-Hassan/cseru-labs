#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);

    /**
     * In this program I will create total 4 process, 1 is the master process and rest of the process are
     * child process. All 3 child processes are taken sum items of number sum it and return it to master
     * process, finally master process add up all the sub sum and print the total value.
     */

    //!!WARNING: This program is not a generalize solution. You should be careful about data items.
    //!!INFO: Here is take total 12 data items and divided all data items by 4, so each sections
    //        contains equal number of data items

    int np = 4; // number of process
    int items = 12;
    int section = items / (np - 1);
    int sub_array[section + 1];
    int root_process_id = 0;
    int rank;
    MPI_Status status;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    if (rank == root_process_id)
    {
        int data[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
        // Message tags are optional. You can use arbitrary integer values for 
        // them and use whichever semantics you like and seem useful to you.

        // int MPI_Send(const void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)
        MPI_Send(data, section, MPI_INT, 1, 0, MPI_COMM_WORLD);
        MPI_Send(data + (section * 1), section , MPI_INT, 2, 0, MPI_COMM_WORLD);
        MPI_Send(data + (section * 2), section, MPI_INT, 3, 0, MPI_COMM_WORLD);

        int total = 0;
        for (int i = 1; i <= 3; i++) { 
            int psum = 0;
            MPI_Recv(&psum, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

            total += psum;
        }

        printf("Total = %d\n", total);

    } else {
        MPI_Recv(&sub_array, section, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
        int sum = 0;

        for (int i = 0; i < section; i++) {
            sum += sub_array[i];
        }
        printf("Total sub array sum: %d\n", sum);
        MPI_Send(&sum, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    }

    MPI_Finalize();
    return 0;
}