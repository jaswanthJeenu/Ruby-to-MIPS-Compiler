.data
f1: .word 0
a1: .word 0
b1: .word 0
c1: .word 0
e1: .word 0
d1: .word 0
.text
main: 
L1: 
addi $s7,$0,-4
L2: 
addi $s6,$0,5
L3: 
xor $s5,$s7,$s6
L4: 
nor $s4,$s7,$s6
L5: 
sllv $s3,$s7,$s6
L6: 
srav $s2,$s7,$s6
sw $s7,a1
sw $s6,b1
L7: 
li $v0, 1
move $a0, $s5
syscall
sw $s5,c1
L8: 
li $v0, 1
move $a0, $s4
syscall
sw $s4,d1
L9: 
li $v0, 1
move $a0, $s3
syscall
sw $s3,e1
L10: 
li $v0, 1
move $a0, $s2
syscall
sw $s2,f1
L11: 
li $v0, 10
syscall
