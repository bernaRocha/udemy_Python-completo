from os import system
system('clear')

# 1
def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

print(saudacao('Oi, tudo bem?', "Fulano"))

# 2
def somatorio(num_1, num_2, num_3):
    return num_1 + num_2 + num_3
print(somatorio(1, 2, 5)) # 8

# 3
def soma_percentual(valor, percentual):
    percentual = (percentual / 100) * valor
    return (valor + percentual)

print(soma_percentual(100, 50)) # 150.0

# 4
def fizzbuzz(parametro):
    if parametro % 3 == 0 and parametro % 5 == 0:
        return 'FizzBuzz'
    if parametro % 5 == 0:
        return 'Buzz'
    if parametro % 3 == 0 :
        return 'Fizz'
    return parametro
 
print(fizzbuzz(15)) # FizzBuzz
print(fizzbuzz(10)) # Buzz
print(fizzbuzz(124)) # 124
print(fizzbuzz(7)) # 7
print(fizzbuzz(10)) # Buzz
