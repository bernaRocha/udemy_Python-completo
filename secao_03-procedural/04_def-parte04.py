from os import system
system('clear')


valor = 'valor'

print(valor) # valor

def func():
    print(valor)

def func2():
    valor = 'Outro valor'
    print(valor)

func() # valor
func2() # Outro valor