# -*- coding: utf-8 -*-

d={'a':1,'b':2,'c':3}
for key in d:
	print(key)
	
for value in d.values():
	print(value)
	
for k,v in d.items():
	print(k,v)
	
#如何判断一个对象是可迭代对象呢？
#方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance(123,Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对
#这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A','B','C']):
	print(i,value)
print('\n')

#同时引用了3个变量
for i,value in enumerate([(1,1),(2,4),(3,9)]):
	print(i,value[0],value[1])
print('\n')