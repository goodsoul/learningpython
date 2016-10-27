# -*- coding: utf-8 -*-

s1 = 72
s2 = 85
r=(s2-s1)/s1*100
print('%.1f' %r)

s = 'Python-中文' 
print(s) 
b = s.encode('utf-8') 
print(b) #b'Python-\xe4\xb8\xad\xe6\x96\x87'
print(b.decode('utf-8')) 
