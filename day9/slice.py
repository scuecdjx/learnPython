#-*- coding:utf-8 -*-
#切片练习

L=['a','b','c','d']

#循环方式提取前三元素
r=[]
n=3
for i in range(n):
	r.append(L[i])
print(r)

#切片方式提取前三元素
print(L[0:3]) #取0，1，2元素
print(L[-3:-1]) #倒数切片，为0可以省略

#创建一个0-99的数列
nums=list(range(100))
print(nums[:10]) 	#前十个数
print(nums[-10:]) 	#后十个数
print(nums[10:20])	#10-19个数
print(nums[:10:2])	#前十个数，每2取一个
print(nums[::5])	#所有数每5个取一个数
n2=nums[:]		#复制
print((0,1,2,3,4,5)[:3]) #tuple也可以切片

