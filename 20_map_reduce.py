# -*- coding: utf-8 -*-
from functools import reduce

def f(x):
	return x*x

#map
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator
#Iterator是惰性序列，通过list()函数让它把整个序列都计算出来并返回一个list	
l=[1,2,3,4,5,6,7,8,9]
r=map(f,l)
print(list(r))

L=[]
for n in [1,2,3,4,5,6,7,8,9]:
	L.append(f(n))
print(L)

L2=list(map(str,l))
print(L2)

#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
#reduce把结果继续和序列的下一个元素做累积计算
def add(x,y):
	return x+y

def multi(x,y):
	return x*y

l_d=[1,2,3,4,5]

#累加
l_d_2=reduce(add,l_d)
#累乘
l_d_3=reduce(multi,l_d)
print(l_d_2)
print(l_d_3)

#练习：
#1.利用map()函数，把用户输入的不规范的英文名字
#变为首字母大写，其他小写的规范名字
L1 = ['adam', 'LISA', 'barT']

#capitalize首字母大写，其余小写
def normalize(name):
	return name.capitalize()
print(list(map(normalize,L1)))

#2.编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
L2_P = [3,5,7,9]
def prod(L):
	def f_n(x,y):
		return x*y
	return reduce(f_n,L)
		
print('L2_P = ',prod(L2_P))
	
#3.利用map和reduce编写一个str2float函数，
#把字符串'123.456'转换成浮点数123.456
from functools import reduce

def str2float(s):
	n=len(s)-s.find('.')
	def fn(x,y):
		return x*10+y		
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}[s]
	return reduce(fn,map(char2num,s))/10

L3='12.3456'	
print (str2float,L3)
print (L3.find('.'))
print (len(L3))