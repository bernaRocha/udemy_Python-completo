from os import system
system('clear')

multiplicacao = lambda x, y: x * y

print(multiplicacao(2, 8))

produtos = [['p1', 56], 
            ['p2', 32], 
            ['p3', 12], 
            ['p4', 18], 
            ['p5', 1]
]

def ordenar(item):
    return item[1]

produtos.sort(key=ordenar, reverse=True)
print(f'Ordenado pelo mais caro: {produtos}')

mais_barato_primeiro = produtos.sort(key=ordenar)
print(f'Ordenado pelo mais barato: {produtos}')

#### com lambda
produtos.sort(key=lambda item: item[1])
print(f'Em ordem crescente de preços: {produtos}')

produtos.sort(key=lambda item: item[1], reverse=True)
print(f'Em ordem decrescente de preços: {produtos}')

#### com sorted
print('Ordem reversa de produtos: ', end=' ')
print(sorted(produtos, key=lambda i: i[0], reverse=True))
