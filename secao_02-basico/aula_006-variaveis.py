nome = input('Digite seu nome: ')
idade = int(input('Sua idade: '))
altura = float(input('Sua altura(x.xx cm): '))
peso = float(input('Quanto está pesando no momento: '))

imc = (peso / altura ** 2)

print(f'{nome} tem {idade} anos, mede {altura}cm e seu imc é {imc:.2f}')