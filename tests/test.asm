section data
    hello: db "Hi Mom!", 10
    helloLen: equ $-hello

section text
    global _start

_start:
    ld a, 1 ; sys_write
    ld bc, 1 ; stdout
    ld de, hello ; message to write
    ld hl, helloLen ; length of message
    rst 38h ; call kernel

    ; end program
    ld a, 60 ; sys_exit
    ld bc, 0 ; exit code
    rst 38h ; call kernel
