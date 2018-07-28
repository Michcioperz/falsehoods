void _start() {
  int ret;
  asm volatile ("syscall" : "=r"(ret) : "a"(60), "D"(1));
}
