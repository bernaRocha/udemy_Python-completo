from os import system
system('clear')

hora_atual = input("Diga a hora atual (0-23): ")

if hora_atual.isdigit():
    hora_atual = int(hora_atual)


    if  hora_atual < 0 or hora_atual > 23:
        print("Horário invlálido!")
    else:
        if hora_atual <= 11:
            print('Bom dia!')
        elif hora_atual <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
    
else:
    print("Horário inválido")
