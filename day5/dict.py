# -*- coding:utf-8 -*-
d={'michael':95,'bob':75,'tracy':85}	#定义一个字典
d['michael']=88		#通过key放入
print(d['michael'])
a='Thomas' in d	#查找Thomas
print(a)
print(d.get('Thomas'))
print(d.get('Thomas',False))
d.pop('bob')
print(d)
