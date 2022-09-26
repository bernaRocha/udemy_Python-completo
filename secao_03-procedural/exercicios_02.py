from os import system
system('clear')

# 01
def ola_funcao():
    return 'Olá mundo - primeira função'

def funcao_mestre(funcao):
    return funcao()

print(funcao_mestre(ola_funcao)) # Olá mundo - primeira função
print(ola_funcao()) # Olá mundo - primeira função

# 02

def mestre(funcao02, *args, **kwargs):
    return funcao02(*args, **kwargs)

def fala_tchau(nome):
    return f'Tchau {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

print(mestre(fala_tchau, 'Fulano')) # Tchau Fulano
print(saudacao('Beltrano', 'tchau')) # tchau Beltrano
