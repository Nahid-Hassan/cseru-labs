# Viva Question and Solutions

## Process

**What is a process**:

```text
* A process is basically a program in execution.
```

**How process stored in RAM/Memory**:

![images](./images/process_components.jpg)

**Process Life Cycle**:

- Start
- Ready
- Running
- Waiting
- Terminate

![images](images/process_state.jpg)

**Process Control Block (PCB)**:

A Process Control Block is a data structure maintained by the Operating System for every process. The **PCB is identified by an integer process ID (PID)**. A PCB keeps all the information needed to keep track of a process

## Signal in OS

What is a signal?

- A signal is a message that is sent to a process to tell it to perform a specific task. Such as to terminate a process, to suspend a process, to resume a process, etc. The signal is sent to the process by the Operating System.

-  The kernel may pass an interrupt as a signal to the process that caused it (typical examples are SIGSEGV, SIGBUS, SIGILL and SIGFPE).

- An process can send signal itself vai kill().


## Deadlock

What is a deadlock? A

- Deadlock is a situation where two or more processes are waiting for each other to complete a task.
- To avoid a deadlock we use bankers algorithm.

![images](./images/presentation7-5.jpg)

## Threading

**What is a threading?**: A thread is a separate execution context in a process. A process can have multiple threads. A thread can be a process that is executing a single function.

**Advantages of Thread**:

- **Threads minimize the context switching time**.
- Use of threads provides concurrency within a process.
- Efficient communication.
- It is more **economical** to create and context switch threads.
- Threads allow **utilization of multiprocessor architectures** to a greater scale and efficiency.

**Types of Thread**:

Threads are implemented in following two ways −

- **User Level Threads** (User managed threads.)

**Advantages**:

- Thread switching does not require Kernel mode privileges.
- User level thread can run on any operating system.

**Disadvantages**:

- In a typical operating system, most system calls are blocking.
- Multithreaded application cannot take advantage of multiprocessing.

- **Kernel Level Threads** − (Operating System managed threads acting on kernel, an operating system core.)

## IPC (Inter Process Communication)

**What is IPC**: Inter process communication is the mechanism by which two processes can exchange data. It is also known as message passing.


**Approaches to Interprocess Communication**:

- **Pipe**: Pipe is a unidirectional communication channel. Two process bi-directional we need two pipes. Pipe are two types:

    - Named Pipe
    - Unnamed Pipe

- **Socket**: The socket is the endpoint for sending or receiving data in a network. It is bi-directional communication channel.

> Most of the operating systems use sockets for interprocess communication.

- **Signal**: Already talked about.
- **Shared Memory**: Shared memory is a memory segment that is shared between processes.

**Synchronization in Interprocess Communication**:

**Semaphore**:

- A semaphore is a variable that is used to control access to a shared resource.
- The two types of semaphores are
  - **binary semaphores** and
  - **counting semaphores**.

**Mutual Exclusion**

Mutual exclusion requires that only one process thread can enter the critical section at a time. This is useful for synchronization and also prevents race conditions.


## Process Synchronization

