#-*- coding:utf-8 -*-
#函数作为返回值
def calcSum(args): #普通计算加和函数
	ax=0
	for n in args:
		ax=ax+n
	return ax

L=[1,2,3,4,5,6]
print(calcSum(L))

def lazySum(*args): #返回一个求和函数，调用时才计算
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum #称为闭包Closure
f=lazySum(1,3,5,7,9) #lazySum返回一个函数
print(f())

f1=lazySum(1,3,5,7,9)
f2=lazySum(1,3,5,7,9)
print(f1==f2) #每次调用都会返回新函数，即使参数相同

#闭包
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
'''闭包不要引用循环变量，否则会发生变化'''

#已绑定的函数参数值不变
def count():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1,f2,f3=count()
print(f1())
print(f2())
print(f3())

#可用lambda函数简化
def createCounter():
	createCounter.n=0 #命名全局变量
	def counter():
	#	nonlocal k #去外部获取n
		createCounter.n += 1
		return createCounter.n	
	return counter
a=createCounter()
print(a(),a())
