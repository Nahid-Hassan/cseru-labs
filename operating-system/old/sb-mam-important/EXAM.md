# Operating System Exam Preparation

- Question Solution
- Topics List
- Assignment & CT Question Solution


Resources: https://drive.google.com/drive/folders/15gq-_qAjUjGZS9__UMdeoUWU0Rdppgte?usp=sharing 

## Question 2017

**Question#1**:
-------


a) **Operating System (OS)** is a system software which manages computer resources (harware, software) and provides an environment where application software can run in order to full-fill users’ demands.

Service Of OS: Slide-1 (Function of OS)

b) PCB : Slide-2 (Intro Process)
c) Kernel: the one program running at all times on the computer.

**Question#2**:
-------

    a, c, d Solutions are in Slide - 2

b) Added Soon

**Question#3**:
-------

a. Solution

```
              P1
            /    \
          /       \
         c1         p1
        / \        /  \
       /   \      /    \
      c2   c1    C3    P1
```

b. Solution
```c
#include <stdio.h>
#include <unistd.h>

int main() {
    int a = 5;
    pid_t cid, mypid;

    mypid = getpid();
    cid = fork();

    if (cid == 0) {
        printf("My PID: %d and my parents pid = %d\n", mypid, getppid()); // different
        a = a - 5;
        printf("a = %d\n", a); // 0
    } else {
        printf("My PID: %d and my parents pid = %d\n", mypid, getppid()); // same
        a = a + 5;
        printf("a = %d\n", a); // 10
        while(1);
    }
}
```
1. Continue execute 

My PID: 185778 and my parents pid = 185586
a = 10  
My PID: 185778 and my parents pid = 185778
a = 0

2.  
- a. Stop Execution - Same output
- b. Show output and wait : Orphan child, parent kill
- c. Stop execution - same output 
- d. Continue Execution - same output

Question#4
-----------------

b. 
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>



int main() {
    int x = 5;
    printf("Hello %d\n", getpid());
    execlp("/bin/cat", "/bin/cat", "./Hi.c", NULL);
    printf("%d + 2 : %d\n", x, x + 2);
}
```

**Output**:

```
Output: Hello 186943
#include <stdio.h>

int main() {
    printf("I executing through child process.\n");
}
```