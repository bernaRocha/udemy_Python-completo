hora_atual = float(print("Diga a hora atual?"))

if 0 < hora_atual and hora_atual < 11:
    print("Bom dia!")
elif 12 < hora_atual < 17:
    print("Boa tarde")
elif 18 < hora_atual < 24:
    print("Boa noite")
else:
    print("Horário inválido")