# -*-coding:utf-8 -*-
#函数的参数

#计算平方
def power(x):
	return x*x

print(power(5))
#计算次方
def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
print(power(5,3))
'''	测试
	print(power(6))
'''

#设置默认参数
'''
	必选参数在前，默认参数在后
	变化大的参数放前面，变化小的放后面
'''
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
print(power(6))

def enroll(name,gender): #学生注册
	print('name:',name)
	print('gender:',gender)
enroll('James','M')
def enroll(name,gender,age=18,city='Beijing'): #设置默认参数
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
enroll('James:','M',7)

#默认参数的误区
def add_end(L=[]):
	L.append('END')
	print(L)
	return L
add_end([1,2,3]) #正常情况
add_end()
add_end() #发生异常

#修改
def add_end(L=None):
	if L is None:
		L=[]
	L.append('sb')
	print(L)
	return L
add_end()
add_end()

#可变参数
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
print(calc([1,2,3]))

#练习题目，接收一个或多个数并计算乘积
def product(*x):
	sum=1 #保存结果
	for i in x:
		sum=sum*i
	return sum
print('product(5,6,7,9)=',product(5,6,7,9))

