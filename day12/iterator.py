#-*- coding:utf-8 -*-
from collections import Iterable
print(isinstance([],Iterable))
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
'''
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next（）函数的对象都是Iterator类型，它们便是一个惰性计算的序列；
集合数据类型如list/dict/str等是Iterable但不是Iterator，不过可以通过iter（）
函数获得一个Iterator对象
Python的for循环本质就是通过不断调用next（）函数实现的，e.g.
'''
for x in [1,2,3,4]
	pass

#等价于
it =iter([1,2,3,4]) #获得Iterator对象
while True:	    #进入循环
	try:
		x=next() #获取下一个值
	except StopIteration: #异常后退出
		break
