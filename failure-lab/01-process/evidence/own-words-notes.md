# Background process

```bash
sleep 600 &
```

The above command will create a background process (`&`) of `sleep` for 600 seconds.

## `$!`

Saves the PID of the most recently started bg job.

For eg we have started the `sleep 600 &`.

You can check the process id and cmd which is being executed using:

```bash
ps -p "$!" -o pid,cmd
```

Process ID value stays the same until you start another background job. If the process exits, `$!` still contains its PID; it doesn’t automatically clear or switch to another process.

## `$$`

It  is the PID of the current shell.

usually current shell is a descendant of PID 1, but it’s not necessarily PID 1’s direct child. It may be started through several processes

for example, a terminal or shell launcher.

Check the shell’s immediate parent with:

```bash
ps -o pid,ppid,cmd -p "$$"
```

Here `PPID` is the `PID` of your shell’s direct parent. 

To see the process tree:

```bash
pstree -sp "$$"
```



## `printf '%s\n'`

printf formats and prints text.

%s is a placeholder for a string.

\n adds a newline.

For example, 

```bash
printf '%s\n' hello
``` 

prints hello followed by a newline.

`printf 'Current Shell PID: %s\nSleep PID: %s\n' "$$" "$!" | tee evidence/lab.pid`

```bash
ps -ef | head -n 12
ps -p "$LAB_PID" -o user,pid,ppid,stat,pcpu,pmem,rss,vsz,etime,comm,args | tee evidence/ps-snapshot.txt
grep -E '^(Name|State|Pid|PPid|Threads|VmPeak|VmSize|VmRSS):' "/proc/$LAB_PID/status" | tee evidence/proc-status.txt
top -b -n 1 -p "$LAB_PID" | tee evidence/top-snapshot.txt
```


| Field | Beginner-friendly meaning |
|---|---|
| `PID` | This process’s ID while it exists. |
| `PPID` | The ID of the process that started it; for your lab, often the shell. |
| `USER` | The account the process runs as. It does not necessarily identify the human or program that launched it. |
| `STAT` / `State` | What the process is doing right now. `S` usually means sleeping while waiting; `R` means running or ready to run. |
| `Threads` | How many threads the process has. |
| `VSZ` / `VmSize` | How much virtual address space is mapped or reserved. It does not mean that much RAM is in use. |
| `RSS` / `VmRSS` | An estimate of how much of this process’s memory is currently resident in physical RAM. |
| `VmPeak` | The largest virtual memory size recorded for the process so far. |
| `%MEM` | Roughly, the process’s resident memory as a share of the machine’s physical RAM. |
| `%CPU` | CPU use. `ps` reports a lifetime-based measure; `top` gives a more current snapshot. |
| `etime` | Wall-clock time since the process started, including time spent waiting. |
| `TIME` in `ps -ef` | CPU time accumulated by the process, not its wall-clock lifetime. |