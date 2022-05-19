/**
 * @file read-write.c
 * @author Md. Nahid Hassan
 * @brief
 * @version 0.1
 * @date 2022-01-08
 *
 * @copyright Copyright (c) 2022
 *
 */

#include <unistd.h>

int main() {
    char buffer[5];

    /**
     * @brief read(fd, buf, count)
     * @param fd : file descriptor
     * @param buf : buffer to store the data
     * @param count : number of bytes to read
     *
     * @return number of bytes read
     */
    // same as scanf("%s", buffer);
    int n = read(0, buffer, sizeof(buffer)); // stdin: 0

    /**
     * @brief write(fd, buf, count)
     * @param fd : file descriptor
     * @param buf : buffer to write
     * @param count : number of bytes to write
     *
     * @return number of bytes written
     */
    // same as printf("%s", buffer);
    write(1, buffer, n); // stdout: 1
}
