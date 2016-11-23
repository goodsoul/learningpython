# -*- coding: utf-8 -*-

l=[36, 5, -12, 9, -21]
l_s=sorted(l, key=abs)
print(l)
print("sorted by abs: ",l_s)

name=['bob', 'about', 'Zoo', 'Credit']
name_s=sorted(name, key=str.lower)
print(name)
print("sorted by str.lower", name_s)

#order by desc
name_s_r=sorted(name, key=str.lower,reverse=True)
print("sorted by str.lower reverse", name_s_r)
print("/n")

#练习:

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#用sorted()对上述列表分别按名字排序

L_S_N=sorted(L,key=lambda x:x[0])
print(L_S_N)

L_S_S=sorted(L,key=lambda x:x[1],reverse=True)
print(L_S_S)

def return_name(t)
	return t[0]
	


