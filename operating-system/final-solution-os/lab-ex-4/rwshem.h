/**
 * Simple Step by Step C Program to demonstrate how to use
    * generate Key
    * using shmget() create block of shared memory
    * using shmat() attach shared memory to process
    * read/write to shared memory
    * using shmdt() detach shared memory from process
*/


/* take result variable as input */
void write_to_shm(int x) {
    key_t key = 1234;

    /* using key, create a block of shared memory */
    int sid = shmget(key, 1024, 0666 | IPC_CREAT);

    /* attach shared memory to a pointer */
    char *shm = shmat(sid, NULL, 0);

    /* write to shared memory */
    sprintf(shm, "%d", x);   /* x is the result variable */

    /* detach shared memory */
    shmdt(shm);
}

int read_from_shm(void) {
    key_t key = 1234;

    /* using key, create a block of shared memory */
    int sid = shmget(key, 1024, 0666 | IPC_CREAT);

    /* attach shared memory to a pointer */
    char *shm = shmat(sid, NULL, 0);

    /* read from shared memory */
    int x = atoi(shm);

    /* detach shared memory */
    shmdt(shm);

    return x;
}