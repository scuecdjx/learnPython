#-*- coding:utf-8 -*-
'''
map()函数接受两个参数，一个是函数，一个是Iterable
map将传入的函数依次作用到序列的每个元素，返回新的
Iterable
'''
def f(x):
	return x*x
r= map(f,[1,2,3,4,5])
print r

#也可以用循环
L=[]
for n in [1,2,3,4,5]:
	L.append(f(n))
print L

#将所有数字变为字符串只需一行代码
print(map(str,[1,2,3,4,5]))

