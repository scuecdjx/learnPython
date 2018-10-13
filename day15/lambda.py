#-*- coding:utf-8 -*-
a=map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
print a

#lambda表示匿名函数，冒号前的x表示函数参数
#可以把匿名函数值赋给一个变量，再利用变量来调用
f=lambda x:x*x
print(f(5))

#也可以把匿名函数当作返回值
def build(x,y):
	return lambda :x*x+y*y
a=build(1,3)
print(a())

#用匿名函数改造代码
'''
def isOdd(n):
	return n%2==1
L=list(filter(isOdd,range(1,20)))
'''
L=list(filter(lambda x:x%2==1,range(1,20)))
print L
