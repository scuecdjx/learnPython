#-*- coding:utf-8 -*-
'''
定制类的运用
'''

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):  #返回用户看到的字符串
        return 'Student object(name:%s)'%self.name
    __repr__ = __str__  #__repr__是返回调试用的字符串
print(Student('djx'))
s= Student('djx')


#__Iter__的用法
class Fib(object): #斐波那契数列
    def __init__(self):
        self.a,self.b=0,1 #初始化两个数
    def __iter__(self):
        return self #实例本身为迭代对象
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b #下一个数
        if self.a>1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)
'''
Fib实例看起来像list，但是无法和list一样用下标取数
可以增加__getitem__方法来达到效果
'''
class Fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
print(f[5])
class Fib(object):
    def __getitem__(self,n): #增加切片功能
        if isinstance(n,int): #n代表索引
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        if isinstance(n,slice): #n是切片的话
            start = n.start #n.start表示切片的开始
            stop = n.stop
            if start is None: #默认切片开头为0
                start = 0
            a,b = 1,1
            L=[] #存放结果的list
            for x in range(stop): 
                if x >= start:
                    L.append(a) #在start和stop之间就增加到L
                a,b = b,a+b
            return L
f2 = Fib()
print(f2[5:10])

#__getattr__  调用不存在的属性
class Student(object):
    def __init__(self):
        self.name = 'djx' #只初始化了一个变量
    def __getattr__(self,attr): 
        if attr=='score': #当调用不存在的变量score时
            return 99

s2 =Student()
print(s2.score)

#动态的调用例子
class Chain(object): #一个API类
    def __init__(self,path=''): #初始化，默认path=’‘
        self.path = path
    def __str__(self):
        return self.path #直接调用时返回
    def __getattr__(self,path): 
        return Chain('%s/%s'%(self.path,path))
    __repr__ = __str__

print(Chain().name)



