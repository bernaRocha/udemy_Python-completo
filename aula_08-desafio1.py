nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))
altura = float(input("Qual sua altura(x.xx cm): "))
peso = float(input("Quanto está pesando atualmente: "))
anoAtual = int(input("Qual o ano atual: "))
anoNascimento = anoAtual - idade
imc = (peso / altura ** 2)

print(f'{nome}, nascido ano de {anoNascimento} tem {idade} anos de idade, mede {altura}cm e um IMC de {imc:.2f}')

"""
Digite seu nome: Bernardo
Qual sua idade: 34
Qual sua altura(x.xx cm): 1.68
Quanto está pesando atualmente: 75
Qual o ano atual: 2022
Bernardo, nascido ano de 1988 tem 34 anos de idade, mede 1.68cm e um IMC de 26.57
"""