from os import system
system('clear')

secreto = 'peremptoriamente'
digitadas = []
chances = 20


while True:
    if chances < 0:
        print('Você perdeu, tente novamente')
        break

    letra = input('Tente uma letra: ').lower()[0]

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" está na palavra')
    else:
        print(f'A letra "{letra}" NÃO está na palavra')
        digitadas.pop()
        chances -= 1 
        print(f'Você ainda tem {chances} chances')

    secreto_tmp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_tmp += letra_secreta
        else:
            secreto_tmp += '*'

    if secreto_tmp == secreto:
        print(f'VocÊ ganhou, a palavra era "{secreto_tmp}"')
        break
    else:
        print(f'A palavra secreta está assim {secreto_tmp}')

    