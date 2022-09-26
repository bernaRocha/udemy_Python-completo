from os import system
system('clear')

def funcao():
    print('Hello world!')

def printar(mensagem):
    print(mensagem)

def com_padrao(mensagem='OI', nome="Fulano"):
    nome = nome.replace('o', '3333')
    print(mensagem, nome)

funcao()
printar('Olá pessoa desenvolvedora')

com_padrao()
com_padrao('Tudo bem?', 'Ciclano')
com_padrao(mensagem="Bora")
com_padrao(nome='Abelardo') # OI Abelard3333
