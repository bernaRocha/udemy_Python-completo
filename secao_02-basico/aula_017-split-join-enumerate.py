from os import system
system('clear')

string = "O Brasil é o país da urna eletrônica, delícia de urna"

lista = string.split(' ')
lista2 = string.split(',')

print(lista)  # ['O', 'Brasil', 'é', 'o', 'país', 'da', 'urna', 'eletrônica,', 'delícia', 'de', 'urna']
print(lista2) # ['O Brasil é o país da urna eletrônica', ' delícia de urna']

termo = ''
contador = 0

for palavra in lista:
    qtd_vezes = lista.count(palavra)
    
    if qtd_vezes > contador:
        contador = qtd_vezes    
        termo = palavra

print(f'A palavra "{palavra}" apareceu {contador}x na frase') # A palavra "urna" apareceu 2x na frase

outra_string = "Estou cansando para palavrão grande"
lista2 = outra_string.split(' ')
outra_string_02 = ',,'.join(lista2)

print(outra_string)    # Estou cansando para palavrão grande
print(lista2)          # ['Estou', 'cansando', 'para', 'palavrão', 'grande']
print(outra_string_02) # Estou,,cansando,,para,,palavrão,,grande

#### enumerate
lista3 = ['Fulano', 'Beltrano', 'Ciclano']

for indice, nome in enumerate(lista3):
    print(indice, nome)
'''
0 Fulano
1 Beltrano
2 Ciclano
'''

enumerada =  enumerate(lista3)
print(list(enumerada)) # [(0, 'Fulano'), (1, 'Beltrano'), (2, 'Ciclano')]
