#-*- coding:utf-8 -*-
# 生成器
L=[x*x for x in range(10)] #列表生成式
L=(x*x for x in range(10)) #生成器

for n in L:	#for循环迭代输出生成器generator
	print(n)

#函数生成斐波拉其数列
def fib(max):
	n=0
	a=0
	b=1
	while n<max:
		print(b) #改为yield b则函数变成generator
		a,b=b,a+b
		n=n+1
	return 'done'
fib(6)
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 5
o=odd()
for n in o:
	pass
