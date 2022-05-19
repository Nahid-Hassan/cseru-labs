/**
 * @file zombie.c
 * @author your name (Md. Nahid Hassan)
 * @brief A zombie process is a process that has terminated but is still in the process table.
 * @version 0.1
 * @date 2022-01-08
 *
 * @copyright Copyright (c) 2022
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

int main(int argc, char *argv[]) {
  printf("Hi i from another source file\n");
}
