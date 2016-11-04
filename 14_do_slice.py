# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

L[:3] #L[0:3]
L[-1] #取最后一个数

L2 = list(range(100))
print(L2[:10])
print(L2[-10:])
print(L2[10:20])
print(L2[:10:2]) #前10个数，每两个取一个
print(L2[::5]) #所有数，每5个取一个

#字符串'xxx'也可以看成是一种list
print('ABCDEFG'[::2])
