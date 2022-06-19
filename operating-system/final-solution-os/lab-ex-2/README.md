### Experiment - 2

```
1. Create a process, named PipeCreator, which can take 'n' number of name from the terminals and create 'n' named pipes.

2. Create two process named 'Minu' and 'Binu' which communicates via a named pipe created by PipeCreator.
Both process takes pipe name via terminals.

2.1) At first Minu will send its PID, its Parent's PID, and a Hello message to Binu via the common named pipe.
     Binu will display all messages received from Minu via the common named pipe in its shell.

2.2) After introductory message Minu will send message which user will type in the terminal.
     Binu will send message to Minu only once and that will be 'Bye'.
     Both Minu and Binu will terminate when they will receive 'Bye' message from the other side.

     For Minu, the user will type 'Bye' message.
     Binu will send static 'Bye' message to 'Minu' after getting 'Bye'  message from Minu.
```

**Understand Problem**: Firstly using `PipeCreator` program -> that takes n name as argument and create n named pipe.
After that we create two process name `Minu` and `Binu`. At first `Minu` send a message that contains its `pid, ppid and hello_message` for **Binu**. Both Minu and Binu are talking with each other via same named pipe. Every time `Minu` send message and `Binu` show in her terminal. If `Minu` send `bye` message than first time `Binu` send `bye` message to `Minu` and `Minu` read it and both are killed.  

**Files**:

- `./PipeCreator.c`
- `./Minu.c` & 
- `./Binu.c`

**Explanation**:

1. **Create Pipe**:

- Using `mkfifo(argv[i], 0777)         // argv[i] contains the name of the pipe` we create pipe.

2. **Open Pipe and Send Message**:

```c
    int fd = open(argv[1], O_WRONLY);
    if (fd == -1) {
        perror("[open] - Pipe opening failed.\n");
        return 1;
    }

    /* write message to pipe */
    write(fd, msg, strlen(msg) + 1);
    close(fd);
```

3. **Open Pipe and Read Message**:

```c
        int fd = open(argv[1], O_RDONLY);
        read(fd, buffer, 100);
        close(fd);

        printf("%s\n", buffer);
```

**Note**: Every time when open pipe it is very very important to notice that `the pipe is only open for reading or writing purpose.` Every time when you `open pipe`, after works done `pipe must be closed`.


**General Syntax**:

```text
     int fd = open(pipe, read/write)

     read(fd, buffer, buffer_size); 
     or 
     write(fd, message, message_size);

     close(fd);
```
![images](images/1.png)