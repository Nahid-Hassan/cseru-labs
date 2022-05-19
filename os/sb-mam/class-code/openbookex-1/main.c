#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <fcntl.h>
#include <string.h>
#include <sys/stat.h>

static int count = 0;

void main(int argc, char *argv[]){
    printf("%d\n", argc);
	for (int i = 0; i <argc;  i++)
        fork();
}
