#-*- coding:utf-8 -*-
#filter()函数用于过滤序列

'''
filter()接受一个函数和一个序列，根据返回值
是True或False来决定保留或删除
'''
def is_odd(n):
	return n%2==1

print(filter(is_odd,[1,2,4,5,6,9,10,15]))

#把一个序列的空字符串删掉
def notEmpty(s):
	return s and s.strip() #strip为删除头尾指定参数的字符串
print(filter(notEmpty,['a','',None,'d','  ']))

'''
用筛选法计算全体素数
'''


#代码有问题
'''def _odd_iter(): #构造无穷数列
	n=1
	while True:
		n=n+2
		yield n

def _not_divisible(n): #筛选函数
	return lambda x:x % n > 0

def primes(): #生成器，返回下一个素数
	yield 2
	it = _odd_iter() #初始序列
	while True:
		n=next(it) #返回序列的第一个数
		yield n
		it = filter(_not_divisible(n),it) #构造新序列
for n in primes():
	if n<10: #输出1000以内的素数
		print(n)
	else:
		break
'''

#练习，找回数
def is_palindrome(n):
	return n==int(str(n)[::-1])
output = filter(is_palindrome,range(1,1000))
print('1-1000',list(output))
if list(filter(is_palindrome,range(1,200)))==[1,2,3,4,5,6,7,8,9,11,22,33,44,
55,66,77,88,99,101,111,121,131,141,151,161,171,181,191]:
	print('yes')
else:
	print('lose')
