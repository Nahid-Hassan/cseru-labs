# Linux System Calls

- [Linux System Calls](#linux-system-calls)
  - [`read` & `write` system call](#read--write-system-call)
  - [`open` system call](#open-system-call)

## `read` & `write` system call

`More details on ./read-write.c`

```c
#include <unistd.h>

int main() {
    char buffer[5];

    // same as scanf("%s", buffer);
    int n = read(0, buffer, sizeof(buffer)); // stdin: 0

    // same as printf("%s", buffer);
    write(1, buffer, n); // stdout: 1
}
```

## `open` system call

`More details on ./open.c`

```c
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main()
{
    int fd = open("./text_file.txt", O_RDONLY); // 3, file found
    // printf("%d\n", fd); // 3

    // int fd2 = open("./new_file.txt", O_CREAT | O_WRONLY, 0624); // 4, file created
    // printf("%d\n", fd2); // 4
    int fd2 = open("./new_file.txt", O_WRONLY);

    char buffer[50];
    int n = read(fd, buffer, sizeof(buffer));
    write(fd2, buffer, n);
}
```
