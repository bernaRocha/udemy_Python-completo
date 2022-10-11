from os import system
system('clear')

'''
append, insert, pop, del, clear, extend, + 
min, max, 
range
'''

lista = ['a', 'b', 'c', 'd', 'e', True, 10.5]
print(lista[-1])

# inverter
print(lista[::-1])

lista01 = [1, 2, 3, 4, 5, 6]
lista02 = [7, 8, 9, 10]

lista01.extend(lista02)
print(lista01) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lista01.extend(False)
#print(lista01) 
##### TypeError: 'bool' object is not iterable

lista01.append(True)
print(lista01) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, True]

lista02.insert(4, 'Número')
print(lista02) # [7, 8, 9, 10, 'Número']

print(max(lista01)) # 10
print(min(lista01)) # 1

multiplos_03 = list(range(0, 100, 3))
print(multiplos_03) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 
#48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
