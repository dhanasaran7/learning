# Process autopsy: harmless `sleep`

Date: 2026-11-19
Objective: to run a harmless sleep process for 600 seconds on background
What I expected: run sleep process on bg
What I tried: sleep 600 & and checked the pid ppid of that process and current shell. Refer to [own-words-notes.md](./own-words-notes.md).
What I observed: saw the pid and ppid state of the process cpu utilization is less because this is harmless process and it is in S state meaning sleep state
$! gives the last ran bg process pid and $$ gives the pid of current shell 
My hypothesis:
Evidence: [own-words-notes.md](./own-words-notes.md)
Root cause / best current explanation:
Fix or result: just a observation test
Prevention / limitations: NA
What I learned: learned about the process PID PPID boot process STATE of process
What remains unclear: pcpu,pmem,rss,vsz,etime,comm
Next step: learn about this deeply along with my current learning structure


## Evidence correction

The process inspected in ps, /proc, and top had PID 2749.

The lab.pid file recorded PID 1284, which does not match the inspected process.
That PID is stale or belongs to a different background job, so I must not use it later
to kill a process.

A process keeps its PID while it is alive.
$! is a shell variable that changes when I start a new background job.

## My process observation

The inspected process was `sleep 600`.

- PID 2749 means: process ID of sleep

- PPID 542 means: the parent process ID of this `sleep` process. In this lab, PID 542 was my shell, which started `sleep`.

- State S means: interruptible sleep. The process is waiting for an event; here it is waiting for its sleep timer. It is not using a CPU core while waiting.

- Threads 1 means: this process has one thread. A thread is the smallest execution unit that the scheduler can run on a CPU core.

- VmSize 3124 kB means: the total virtual address space mapped or reserved for this process. It can include program code, data, stack, libraries, and other mappings. It does not mean all 3124 kB is using physical RAM.

- VmRSS 1104 kB means: approximately 1104 kB of this process's memory is currently resident in physical RAM.

- %CPU 0.0 means: the process used almost no CPU during this observation because it was waiting. A short startup or shutdown action may still use a tiny amount of CPU.

- ELAPSED 00:13 means: 13 seconds had passed from process start until this snapshot was taken. It is wall-clock time, not CPU time.

## Retrieval questions

1. Why can elapsed time increase while CPU time remains near zero?

Becasue elapsed time is time taken by process from starting to now. But a process may or may not consume the cpu for eg sleep process which doesn't consume the cpu so its cpu time is 0

2. Why is VmSize larger than VmRSS for this process?

VmSize is the process's virtual address space. VmRSS is the part currently resident in physical RAM. VmSize can be larger because many virtual-memory pages may not currently need physical RAM.

3. Why is it unsafe to use an old PID later without checking that it still belongs
   to the intended process?

A process keeps its PID only while it is alive. After it exits, Linux can reuse the same PID for a different process. If I run `kill` using an old PID, I could accidentally target the wrong process. `$!` changing after another background job is a separate issue: it means my shell variable now points to the newest background job.

4. Explain the difference between a program, process, and thread.

A program is a file on disk containing instructions and data.

A process is a running instance of a program. The OS gives it a PID, memory, permissions, open files, and one or more threads.

A thread is one execution path inside a process. The scheduler runs threads on CPU cores.