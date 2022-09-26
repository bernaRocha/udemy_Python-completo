from os import system
system('clear')

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['mensagem'])


lista = [1,2,3,4,5,6, 7, 8, 9]
n1, n2, *n = lista
# a partir do 2 os valores estão em *n
print(n1, n2, *n) # 1 2 3 4 5 6 7 8 9

print(*n) # 3 4 5 6 7 8 9

func(nome='Fulano', mensagem='oi') # Fulano oi
func(nome='Outro nome', mensagem='tchau') # Outro nome tchau
print(*n) # 3 4 5 6 7 8 9
