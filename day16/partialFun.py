#-*- coding:utf-8 -*-
'''
Partial function偏函数可以固定原函数
的部分参数，调用更简单
'''
print(int('12345')) #int函数还有一个base参数
print(int('12345',base=8)) #base=8表示按8进制转换
print(int('12345',16))

def int2(x, base=2): #设置默认base为2
	return int(x,base)

print(int2('100000')) #结果为32

#使用functools.partial创建偏函数
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))
print(int2('1000000',base=10)) #int2本质上还是int函数，不过默认base变了

