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

#for循环调用generator得到返回值
'''g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
'''

'''
练习:利用generator输出杨辉三角
'''
def triangels():
	s=1 #边界
	t=1 #临时变量
	num=[1]
	while True:
		yield num #返回num后继续向下执行
		sum=[] #临时list
		i=0 #临时变量，保存上一次的值
		for num1 in num: #用来计算num里两个元素的和
			sum.append(i+num1) #计算num里两个元素的和
			i=num1 #下一个元素
		sum.append(1) #最后一个元素为1
		num=sum # 得到最后的list
# 期待输出
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
# [1,5,10,10,5,1]
# [1,6,15,20,15,6,1]
# [1,7,21,35,35,21,7,1]
# [1,8,28,56,70,56,28,8,1]
# [1,9,36,84,126,126,84,36,9,1]
n=0
result =[]
for t in triangels():
	print(t)
	result.append(t)
	n=n+1
	if n == 10:
		break
if result==[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1],
 [1,5,10,10,5,1],
 [1,6,15,20,15,6,1],
 [1,7,21,35,35,21,7,1],
 [1,8,28,56,70,56,28,8,1],
 [1,9,36,84,126,126,84,36,9,1]
]:
	print('测试通过')
else:
	print('测试失败')







