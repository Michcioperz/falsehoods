void _start() {
  int ret;
  asm volatile ("syscall" : : "a"(60), "D"(1));
}
