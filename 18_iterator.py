# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

def g():
	yield 1
	yield 2
	yield 3
	
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#集合数据类型如list、dict、str等是Iterable但不是Iterator，
#不过可以通过iter()函数获得一个Iterator对象。

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable)) 
print('Iterable? \'abc\':', isinstance('abc', Iterable)) 
print('Iterable? 123:', isinstance(123, Iterable)) 
print('Iterable? g():', isinstance(g(), Iterable)) 
print('\n')
print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator)) 
print('Iterator? \'abc\':', isinstance('abc', Iterator)) 
print('Iterator? 123:', isinstance(123, Iterator)) 
print('Iterator? g():', isinstance(g(), Iterator)) 
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator)) 
print('\n')

print('for x in [1,2,3,4,5]:')
for x in [1,2,3,4,5]:
	print(x)

print('\n')	
	
print('for x in iter([1,2,3,4,5]):')
for x in [1,2,3,4,5]:
	print(x)
	
print('\n')	
	
print('next():') 
it = iter([1, 2, 3, 4, 5]) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 
print(next(it)) 

#dict
d = {'a': 1, 'b': 2, 'c': 3}

print('\n')	

#iter each key:
print('iter_key:',d)
for k in d.keys():
	print('key:',k)
	
print('\n')	
	
#iter each value:
print('iter_value:',d)
for v in d.values():
	print('value:',v)

print('\n')	
	
#iter both key and value:
print('iter item:', d)
for k,v in d.items():
	print('item:',k,v)
	
print('\n')	

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i,value in enumerate(['A', 'B', 'C']):
	print(i,value)
	
print('\n')		

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x,y)