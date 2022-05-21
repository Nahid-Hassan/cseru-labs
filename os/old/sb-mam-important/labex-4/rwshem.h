void write_to_shm(int x)
{
    key_t key = 1234;
    int sid = shmget(key, 1024, IPC_CREAT | 0666);

    char *str = shmat(sid, NULL, 0);

    char num[10];
    sprintf(num, "%d", x);
    strcpy(str, num);

    shmdt(str);
}

int read_from_shm()
{
    key_t key = 1234;
    int sid = shmget(key, 1024, IPC_CREAT | 0666);

    char *str = shmat(sid, NULL, 0);
    int num = (int)strtol(str, (char **)NULL, 10);
    shmdt(str);

    return num;
}
