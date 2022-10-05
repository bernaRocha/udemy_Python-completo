from pessoa import Pessoa
from os import system
system('clear')

'''
pessoa01 = Pessoa()
pessoa02 = Pessoa()
print(pessoa01) # <pessoa.Pessoa object at 0x7f7c08762c70>
print(pessoa02) # <pessoa.Pessoa object at 0x7f7c08762e80>
'''

pessoa01 = Pessoa('Fulano', 32)
print(pessoa01) # <pessoa.Pessoa object at 0x7f7e46ce6c70>
print(pessoa01.comer('pão com mortadela'))
print(pessoa01.falar('oi')) 
print(pessoa01.parar_comer())
print(pessoa01.falar())