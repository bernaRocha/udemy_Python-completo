from os import system
system('clear')

'''
> - Esquerda
< - Direita
^ - Centro
'''

num_1 = 1
print(f'{num_1:0>10}')  # 0000000001
num_2 = 2
print(f'{num_2:0<5}') # 20000
num_3 = 1150
print(f'{num_3:0^10}') # 0001150000

num_3 = 1150
print(f'{num_3:0^10.2f}') # 01150.0000

nome = 'Fulano'
print(f'{nome:&^20}') # &&&&&&&Fulano&&&&&&&
