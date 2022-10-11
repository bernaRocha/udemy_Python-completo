from nntplib import GroupInfo
from os import system
from tokenize import group
system('clear')

t1 = (1, 2, 3, 'a', 'fulano')

print(type(t1), t1[3]) # <class 'tuple'> a

for valor in t1:
    print(valor, type(valor))
'''
1 <class 'int'>
2 <class 'int'>
3 <class 'int'>
a <class 'str'>
fulano <class 'str'>
'''

t2 = 5,         # a vírgula tranforma em tupla
print(type(t2)) # <class 'tuple'>

print(t1 + t2) # (1, 2, 3, 'a', 'fulano', 5)

# gambiarra para alterar uma tupla
tupla = (1, 2, 3, 4)
tupla = list(tupla)
tupla[0] = 10000
tupla = tuple(tupla)
print(tupla)

# (10000, 2, 3, 4)