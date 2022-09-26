# while True: # nunca vai parar
#     nome = input('Qual seu nome? ')
#     print(f'Olá {nome}!')

x = -7
while x < 10:
    if x == 3:
        x += 1
        continue # para no 2 caso não tenha o incrementador acima x += 1
    
    print(x)
    x += 1
print('acabo')

####################################
y = -3
while y < 10:
    y += 1
    if y == 3:
        
        break 
    
    print(y) # devido o break a instrução não funciona
    
print('acabo')
#####################################
z = 0
while z < 10:
    w = 0

    while w < 3:
        print(f'z vale {z} e w vale {w}')
        w += 1
    
    z += 1

print('Fim')