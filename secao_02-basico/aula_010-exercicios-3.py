from os import system
system('clear')

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f'O nome {nome} é curto')
elif tamanho_nome <= 6:
    print(f'O nome {nome} não é tão curto')
else:
    print(f'Seu nome é {nome} e tem {tamanho_nome} letras')
