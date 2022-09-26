from os import system
system('clear')

def funcao(var):
    return var
    # aqui o código não é executado

variavel = funcao('Valor da função')

if variavel:
    print(variavel)
else:
    print('Valor inválido')

def divisao(n1, n2):
    if n2 == 0:
        return f'Divisão por zero não é possível'
    else:
        return n1 / n2

print(divisao(8, 2), type(divisao)) # 4.0 <class 'function'>
print(divisao(8, 0), type(divisao)) # Divisão por zero não é possível <class 'function'>

def dumb():
    return f

def f(var):
    print(var)

print(dumb(), type(dumb()))  # <function f at 0x7f94d102d940> <class 'function'>
print(dumb()('Outro valor'))
'''
Outro valor
None
'''
variavel = dumb()
print(id(variavel), id(f)) # 139658592385344 139658592385344
