from os import system
system('clear')

#texto = input('Digite o texto para a nálise: ').lower()
texto = 'Python'

'''
for n, letra in enumerate(texto):
     print(n, letra)
0 P
1 y
2 t
3 h
4 o
5 n
'''

for numero in range(0, 10, 2):
    print(numero, end=' ') # 0 2 4 6 8 


for numero in range(30, 10, -2):
    print(numero, end=' ') # 30 28 26 24 22 20 18 16 14 12

for numero in range(0, 100, 14):
    print(numero, end=' ') # 0 14 28 42 56 70 84 98 
    