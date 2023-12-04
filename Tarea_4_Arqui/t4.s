	.data
f: .word 2 @funcion la cual se desea ocupar
x: .word 2 @valor x para funcion 1
n: .word 0 @valor n para funcion 1 o 2


	.text
main:
	ldr r0, =f
	ldr r0, [r0]
	ldr r1, =x
	ldr r1, [r1]
	ldr r2, =n
	ldr r2, [r2]
	cmp r0, #1
	beq fuumo
	bne aureo

@---------------FUNCION FUUMO-------------------@
fuumo:
	cmp r2, #0
	beq iffuumo
	cmp r2, #1
	beq eliffuumo
	b elsefuumo
	
@Clausula if de funcion fuumo
iffuumo:
	mov r3, #0
	mul r3, r3, r1 @r3 = 0*x
	mov r0, #1 @r0 = 1
	add r0, r0, r3 @r0 = 1 + 0*x
	push {r0}
	mov r0, lr
	cmp r0, #0
	pop {r0}
	beq finfuumo
	mov pc, lr

@Clausula elif de funcion fuumo
eliffuumo:
	mov r0, #2 @r0 = 2
	mul r0, r0, r1 @r0 = 2*x
	push {r0}
	mov r0, lr
	cmp r0, #0
	pop {r0}
	beq finfuumo
	mov pc, lr

@Clausula else de funcion fuumo
elsefuumo:
	@guardo todo en r4
	push {r2}
	sub r2, r2, #1  @n-1
	mov r3, #2
	mul r3, r3, r1 @r3 = 2*x
	
	bl fuumo
	mul r3, r3, r0 @r3 = 2*x*fuumo(x,n-1) 
	pop {r2}
	add r4, r4, r3 @r4 += r3
	sub r2, r2, #2
	bl fuumo
	add r2,r2,#1
	mov r3, #2
	mul r3, r3, r2 @r3 = 2*(n-1)
	mul r3, r3, r0 @r3 = 2*(n-1)*fuumo(x,n-2)
	pop {r2}
	add r5, r5, r3 @ r5 += r3
	sub r4, r4, r5 @r4 = 2*x*fuumo(x,n-1) - 2*(n-1)*fuumo(x,n-2)
	mov r0, r4 @r0 += r4 (Para el retorno igual a r0)
	cmp r2, #0
	beq finfuumo	
	sub r2,r2,#1
	bl elsefuumo
	mov pc, lr
	
@Termino funcion fuumo
finfuumo:
	mov r2, r0
	mov r0, #0
	mov r1, #0
	bl printInt
	wfi
@---------------FUNCION FUUMO-------------------@

@---------------FUNCION AUREO-------------------@
aureo:
	push {r2}
	bl lucas
	mov r4, r2 @r4 contiene salida de Lucas
	pop {r2}
	bl fibonacci
	mov r5, r0 @r5 contiene a la salida de fibonacci
	mov r0, #5
	bl qfp_fsqrt @raiz de 5 en r0
	mov r1, r5
	bl qfp_fmul @fibonacci por raiz de 5 en r0
	mov r5, r0 @fibonacci por raiz de 5 en r5
	mov r0, r4
	bl qfp_int2float @Convertir resultado lucas a flotante
	mov r1, r5
	bl qfp_fadd @Lucas + fibonacci por raiz de 5 en r0
	mov r3, r0 @Lucas + fibonacci por raiz de 5 en r3
	mov r0, #1
	mov r1, #2
	bl qfp_fdiv @1/2 en r0
	mov r1, r3
	bl qfp_fmul @(Lucas + fibonacci por raiz de 5)/2 en r0
	bl qfp_float2int
	mov r2, r0
	mov r0, #0
	mov r1, #0
	bl printInt
	wfi
@Funcion lucas
lucas:
	cmp r2, #0
	beq iflucas
	cmp r2, #1
	beq eliflucas
	b elselucas

@Clausula if de funcion lucas
iflucas:
	add r3, #2
	push {r0}
	mov r0, lr
	cmp r0, #0
	pop {r0}
	beq finlucas
	mov pc, lr

@Clausula elif de funcion lucas	
eliflucas:
	add r3, #1
	push {r0}
	mov r0, lr
	cmp r0, #0
	pop {r0}
	beq finlucas
	mov pc, lr

@Clausula else de funcion lucas
elselucas:
	sub r2, r2, #1
	push {r2}
	bl lucas
	pop {r2}
	sub r2, r2, #1
	bl lucas
	pop {r2}
	cmp r2, #1
	beq finlucas
	cmp r2, #0
	beq finlucas
	sub r2, r2, #1
	bl elselucas
	mov pc, lr

@Termino funcion lucas
finlucas:
	mov r2, r3
	mov pc, lr

@Funcion fibonacci
fibonacci: @Llamar a lucas con n+1 y n-1
	mov r3, r2
	add r2, r2, #1
	bl lucas
	mov r5, r2
	cmp r2,#1
	beq resta
	bl lucas
	mov r6, r2
	add r5, r5, r6
	mov r0, r5
	bl qfp_int2float
	mov r2, r0
	mov r0, #1
	mov r1, #5
	bl qfp_fdiv
	mov r1, r2
	bl qfp_fmul
	mov pc, lr
	
resta:
	sub r2, r2, #2
	bl lucas
	mov r6, r2
	add r5, r5, r6
	mov r0, r5
	bl qfp_int2float
	mov r2, r0
	mov r0, #1
	mov r1, #5
	bl qfp_fdiv
	mov r1, r2
	bl qfp_fmul
	mov pc, lr
