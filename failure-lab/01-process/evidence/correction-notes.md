# Evidence correction

The process inspected in `ps`, `/proc`, and `top` had PID `2749`.

The `lab.pid` file recorded PID `1284`, which does not match the inspected process.

PID `1284` is stale historical data from an earlier background job. It must not be used later to stop a process.

A process keeps its own PID while it is alive. `$!` changes when the shell starts a newer background job.