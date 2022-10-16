conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 2100
cheque_especial = 450



if conta_normal:

    if saldo >=saque :
        print("Sacado com sucesso!")
    elif saque <= (saldo+cheque_especial):
        print("Sacado usando cheque especial!")

elif conta_universitaria:
    if saldo>=saque:
        print("Sacado com sucesso!")
    else:
        print("Saldo insuficiente")

else:
    print("Você não é cliente")