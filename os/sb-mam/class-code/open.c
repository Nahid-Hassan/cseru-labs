/**
 * @file open.c
 * @author Md. Nahid Hassan
 * @brief
 * @version 0.1
 * @date 2022-01-08
 *
 * @warning: This program is not tested.
 * @copyright Copyright (c) 2022
 *
 */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

int main()
{
    /**
     * @brief open(pathname, flags, mode) # mode use if creating a file
     * @param pathname : path to the file
     * @param flags : flags to open the file with (O_RDONLY, O_WRONLY, O_RDWR)
     * @return file descriptor
     *
     * @details open() returns a file descriptor that can be used to access the file. The file descriptor is used in subsequent calls to read(), write(), and close(). The file descriptor returned by open() is guaranteed to be greater than 2 (stdin, stdout, stderr).
     *
     */
    /* if file not found return -1, else return file descriptor at least greater than 2. */
    // int fd = open("/home/nahid/Desktop/open.c", O_RDONLY); // -1, file not found
    int fd = open("./text_file.txt", O_RDONLY); // 3, file found
    // printf("%d\n", fd); // 3

    /**
     * @brief open(pathname, flags, mode) # mode use if creating a file
     */

    // int fd2 = open("./new_file.txt", O_CREAT | O_WRONLY, 0624); // 4, file created
    // printf("%d\n", fd2); // 4
    int fd2 = open("./new_file.txt", O_WRONLY);

    char buffer[50];
    int n = read(fd, buffer, sizeof(buffer));
    write(fd2, buffer, n);
}
