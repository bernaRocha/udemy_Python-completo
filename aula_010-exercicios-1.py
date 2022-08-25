# Exercício básico de if e else
# Verificação se número digitado é par ou ímpar
# caso valor digitado não seja um número aparece a mensagem de erro
# exercício resolvido de duas formas distintas na data de 25/08/22

# autor: Bernardo Rocha github:bernaRocha

numero = input("Digite um número inteiro: ")

#  print(type(numero))

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0: 
        print(f'O número {numero} é par')
    else:
        print(f"{numero} não é um número par")
else:
    print(f"O valor digitado '{numero}' não é um número inteiro")

#### resolvendo de forma invertida > comentar acima para rodar

if not numero.isdigit():
    print(f"O valor digitado '{numero}' não é um número inteiro")
else:
    numero = int(numero)

    if not numero % 2 == 0:
        print(f"{numero} não é um número par")
    else:
        print(f'O número {numero} é par')
