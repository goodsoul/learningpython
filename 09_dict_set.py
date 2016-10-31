# -*- coding: utf-8 -*-

#dict
dict={'a':95,'b':90,'c':85,'d':80}
print(dict['c'])

dict.get('a',-1)
dict.get('e',-1)

#set
s=set([1,1,2,2,3,3])
print(s)

s1=set([1,2,3])
s2=set([1,(2,3)])
print(s)
print('s1:',s1)
print('s2:',s2)
print('s1&s2:',(s1&s2))
print('s1|s2:',(s1|s2))
