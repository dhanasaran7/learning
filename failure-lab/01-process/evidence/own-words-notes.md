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

