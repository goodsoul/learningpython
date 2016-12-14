# -*- coding: utf-8 -*-

def int2(x,base=2):
	return int(x,base)
	
print(int2('10'))
print(int2('101'))

import functools
int16=functools.partial(int,base=16)
print(int16('10'))
print(int16('101'))
print('\n')

#创建偏函数时，可接收函数对象、*args和**kw这3个参数：
kw={'base':2}
print(int('100',**kw))

max2 = functools.partial(max,100) #等价于args = (100, 5, 6, 7)
print(max2(5,6,7,8))

# 当函数的参数个数太多，需要简化时，
# 使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。