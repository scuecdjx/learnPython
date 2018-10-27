#-*- coding:utf-8 -*-
'''
错误处理
'''
try:
    print('try...')
    r= 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('End')

try:
    print('try...')
    r= 10/int('2')
    print('result:',r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except ValueError as e:
    print('ValueError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('End')

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
            print('Error:',e)
    finally:
        print('finally...')
main()

import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('End\n')

#练习
from functools import reduce

def str2num(s):
    if s.find('.')==-1: #如果字符串没有找到小数点，返回值为-1
        return int(s)
    else:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except ValueError as e:
        print('ValueError:',e)

main()
