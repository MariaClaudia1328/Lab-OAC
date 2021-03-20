.data

.text
lw  $t0, OFFSET(a$s3)
add $t0,$a2,$t0
sub $t0,$a2,$t0
and $t0,$a2,$t0
or  $t0,$a2,$t0
nor $t0,$a2,$t0
xor $t0,$a2,$t0
sw  $t0, OFFSET($s3)
jr  $t0
jal LABEL
beq $t1, $zero, LABEL
bne $t1,$zero,LABEL
slt $t1,$t2,$t3
lui $t1, 0xXXXX
addu $t1,$t2,$t3
subu $t1,$t2,$t3
sll $t2,$t3,10
srl $t2,$t3,10
addi $t2,$t3,-10
andi $t2,$t3,-10
ori $t2,$t3,-10
xori $t2,$t3,-10
mult $t1, $t2
div $t1, $t2
li $t1, XX 
mfhi $t1
mflo $t1
bgez $t1, LABEL
clo $t1,$t2
srav $t1,$t2,$t3
sra $t2,$t1,10
madd $t1,$t2
msubu $t1,$t2
jalr $t1,$t2
jalr $t1
bgezal $t1, LABEL
addiu $t1,$t2,$t3
lb $t1,$t2,$t3
movn $t1, $t2,$t3
mul $t1,$t2,$t5
sb $t4,1000($t2)
slti $t1,$t2,-100
sltu $t1,$t2,-100
teq $t1,$t2
LABEL: 