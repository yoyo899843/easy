        global    _start

        section   .text
_start:
    mov       rdi, message
    mov       rcx, 0
    jmp       .compare
.loop:
    mov       al, [rdi + rcx]
    xor       al, 0x5a
    mov       [rdi + rcx], al
    inc       rcx
.compare:
    cmp       rcx, 28
    jl        .loop
    mov       rax, 1
    mov       rdi, 1
    mov       rsi, message
    mov       rdx, 29
    syscall
    mov       rax, 60
    xor       rdi, rdi
    syscall

    section   .data
message:    db        28, 22, 27, 29, 33, 13, 8, 19, 14, 31, 5, 15, 5, 21, 13, 20, 5, 27, 9, 9, 31, 23, 24, 22, 3, 123, 123, 39, 10
