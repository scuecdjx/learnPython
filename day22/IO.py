#-*- coding:utf-8 -*-
f = open('/home/scuecdjx/code/python/day20/__str__.py','r')
print(f.read())
f.close()
fpath = r'/home/scuecdjx/code/python/day20/MixIn.py'
with open(fpath,'r') as f:
    s = f.read()
    print(s)