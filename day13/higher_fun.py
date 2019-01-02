#-*- coding:utf-8 -*-
#高阶函数练习
abs(-10)
f=abs #将函数本身当作变量赋给f
print(f(-10)) #输出
#说明函数本身也是函数！

#传入函数，编写高级函数
def add(x,y,f):
	return f(x)+f(y)

print(add(5,-6,abs))
