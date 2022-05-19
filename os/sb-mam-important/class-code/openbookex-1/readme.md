## Question#1

**What happens when a process parent finishes before the child?**:

When a parent process dies before a child process, the kernel knows that it's not going to get a wait call, so instead it makes these processes "orphans" and puts them under the care of init (remember mother of all processes). Init will eventually perform the wait system call for these orphans so they can die.

###  3

```c
$ gcc ProcessCreation.c -o ProcessCreation
$ ./ProcessCreation I love to study Operating System

#include <unistd.h>
void main(int argc, char *argv[]){
	for (int i = 0; i <argc;  i++)
		fork();
}
```

Total process create **128**

agrc = 7
we know 2^n number of process is created.

so 2^7 = 128 process is created.

### 4

new = many
ready = many
running = up to two ... two core
waiting = many
