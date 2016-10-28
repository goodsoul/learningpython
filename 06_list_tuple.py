# -*- coding: utf-8 -*-

#List
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

#Tuple
T = (
    ('Apple', 'Google', 'Microsoft'),
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
)

# List练习:
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

# Tuple练习:
# 打印Apple(Tuple):
print(L[0][0])
# 添加C#:
T[1].append('C#')
print(T[1])
# 添加BILL到T[2]第二位:
print(T[2][1])
T[2].insert(1,'Bill')
print(T[2][1])