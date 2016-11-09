# -*- coding: utf-8 -*-

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
l=[x*x for x in range(1,20) if x%2==0]
print(l)

#还可以使用两层循环，可以生成全排列
l2=[m+n for m in 'ABC' for n in 'XYZ']
print(l2)

#dict的items()可以同时迭代key和value
d={'x':'A', 'y':'B', 'z':'C'}
for k,v in d.items():
	print(k,'=',v)
	
l3=[k+'='+v for k,v in d.items()]
print(l3)

#把一个list中所有的字符串变成大写
print([s.upper() for s in l3])

#练习：使用内建的isinstance函数可以判断一个变量是不是字符串：
L = ['Hello', 'World', 18, 'Apple', None]
L_S=[m for m in L if isinstance(m,str)==True]
L_N=[n for n in L if isinstance(n,str)==False]
print([m.lower() for m in L_S])
print(L_N)