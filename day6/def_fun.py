#-*- coding:utf-8 -*-
#自定义函数#
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-99))
#定义一个空函数
def nop():
  pass


#抛出异常
def my_abs(x):
   if not isinstance(x,(int,float)):
	raise TypeError('bad operand type')
   if x>=0:
	return x
   else:
	return -x
#print(my_abs('a'))

#返回多个值的函数
import math
def move(x,y,step,angle=0):
	nx=x+step * math.cos(angle)
	ny=y-step * math.sin(angle)
	return nx,ny
print(move(100,100,60))

#定义函数求解一元二次方程
def quadratic(a,b,c):
	x1=0.5*(-b+math.sqrt(b*b-4*a*c))/a
	x2=0.5*(-b-math.sqrt(b*b-4*a*c))/a
	return x1,x2
#测试
print('2x^2+3x+1=0\'s solution is',quadratic(2,3,1))

