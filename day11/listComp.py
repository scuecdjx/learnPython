#-*- coding:utf-8 -*-
# 列表生成器的使用

a=list(range(1,11))
print(a)
L=[]
for x in range(1,11):
	L.append(x*x)
print(L)
#列表生成式方法
b=[x*x for x in range(1,11)]
print(b)
c=[x*x for x in range(1,11) if x%2==0] #输出偶数的平方和
print(c)
d=[m+n for m in 'ABC' for n in 'XYZ']
print(d)

import os
e={1:'A',2:'B',3:'c'}
for k,v in e.items():
	print k,' = ',v

#最后把一个list中所有的字符串变小写
L=['Hello','World','IBM','Apple']
L=[s.lower() for s in L]
print(L)

#练习  
'''处理不同数据类型的lisComp,全部转化为小写'''
L=['Hello','World',18,'Apple',None]
L2=[for i in L if isstance]
	

print(L2)
if L2 ==['hello','world','Apple']：
	print('通过')
else:
	print('成功')
