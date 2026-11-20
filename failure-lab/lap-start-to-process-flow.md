# Power on

→ CPU begins running firmware

## Firmware / UEFI

→ performs basic hardware setup, including enough RAM setup to continue

→ runs startup checks such as POST

→ follows its configured boot entry

→ starts a bootloader, such as GRUB

## Bootloader

→ loads the Linux kernel into RAM

→ usually loads initramfs too: a small temporary filesystem in RAM

## Kernel

→ takes control of CPU, memory, scheduling, and device access

→ discovers hardware and uses device drivers

→ mounts the real root filesystem from disk

→ starts the first user-space program: usually systemd, PID 1

## systemd

→ starts and supervises services, networking, login, desktop, etc.

---

**Kernel** = manages the machine’s core resources and enforces permissions

**systemd** = a normal program with a special startup role; it organizes services

---

## You click Chrome

→ desktop launcher asks the kernel to start it

→ a process is created

→ the child process runs execve()

→ execve replaces the child’s old program with Chrome's program

→ the PID stays the same

→ Chrome begins running

---

## Chrome process

```text
Chrome process
├── PID
├── PPID
├── user identity and permissions
├── open files and network connections
├── environment variables
├── current directory
├── one or more threads
└── virtual address space
```

---

Chrome’s virtual address space is its private map of memory addresses. It contains places for program instructions, shared libraries, data, heap, and thread stacks.

---

```text
Chrome uses virtual address 0x...
        ↓
CPU's MMU checks Chrome's page table
        ↓
page table identifies the real location in RAM
        ↓
CPU reads or writes that RAM location
```

---

When Chrome needs a protected OS service, Chrome makes a system call to the kernel. The kernel runs the matching system-call handler and uses drivers when hardware access is needed.

### Example

**Chrome needs to open a file**

→ Chrome makes open() system call

→ kernel checks permissions

→ kernel uses filesystem and storage-driver code

→ kernel returns a file handle to Chrome

**Chrome needs network data**

→ Chrome makes network-related system calls

→ kernel uses the network stack and network driver

→ data arrives in RAM

→ Chrome reads that data from its virtual address space

---

## Revised short explanation

A program is stored on disk. When started, the OS creates a process with a PID, resources, one or more threads, and a private virtual address space. The process’s threads run program instructions on CPU cores. The CPU translates the process’s virtual addresses into physical RAM locations through page tables. When the program needs a protected OS service, it makes a system call to the kernel.

---