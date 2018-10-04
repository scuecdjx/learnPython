#-*- coding:utf-8 -*-
# 通过for来遍历list或tuple叫做迭代
d={'a':1,'b':2,'c':3}
for key in d:
	print(key)

for ch in 'ABC':
	print(ch)
# 判度可迭代对象
from collections import Iterable
print(isinstance('abc',Iterable)) # 字符串是否可迭代
print(isinstance(123,Iterable)) #整数是否可迭代
 
# 两个变量的迭代
for i,value in enumerate(['A','B','C']):
	print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
	print(x,y)


#练习，迭代查找list中最大小值，返回tuple
def findMinAndMax(L):
	if L==[]:
		return(None,None) # 如果是空就返回两个None
	max=L[0] #令第一个元素为最大值，用来比较
	min=max
	for i in L:
		if i>max:	#如果i大于最大值则最大值为i
			max=i
		if i<min:
			min=i
	return(min,max)

#测试
if findMinAndMax([]) != (None,None):
	print(False,1)
elif findMinAndMax([7]) !=(7,7):
	print(False,2)
elif findMinAndMax([7,1])!=(1,7):
	print(False,3)
elif findMinAndMax([7,2,3,5,9])!=(2,9):
	print(False,4)
else:
	print(True)
