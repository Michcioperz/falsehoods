define void @_start() {
  call void asm sideeffect inteldialect "syscall", "{rax},{rdi}"(i64 60, i64 1)
  ret void
}
