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