from os import system
system('clear')

# se o elemento tem índices ele é iterável

frase = 'eu estou cansado para um palavrão'
tamanho_frase = len(frase)
contador = 0
nova_frase = ''

while contador < tamanho_frase:
    #print(frase[contador], contador)
    #nova_frase += frase[contador]
    #print(nova_frase)
    letra = frase[contador] 
    if letra == 'a':
        nova_frase += 'A'
    else:
        nova_frase += letra
    contador += 1
    
print(nova_frase) # eu estou cAnsAdo pArA um pAlAvrão
