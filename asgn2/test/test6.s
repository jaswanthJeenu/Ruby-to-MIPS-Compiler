.data
a: .word 0
c: .word 0
d: .word 0
.text
main: 
L0: 
lw $s7,a
addi $s7,$0,2
sw $s7,a
L1: 
lw $s7,d
addi $s7,$0,1
sw $s7,d
L2: 
jal b
lw $s7,c
move $s7,$v1
sw $s7,c
li $v0,10
syscall
b: 
L4: 
lw $s7,a
lw $s6,d
add $s7,$s7,$s6
sw $s6,d
L5: 
move $v1, $s7
jr $ra
sw $s7,a
L6: 
li $v0, 1
lw $s7,c
move $a0, $s7
syscall
sw $s7,c

