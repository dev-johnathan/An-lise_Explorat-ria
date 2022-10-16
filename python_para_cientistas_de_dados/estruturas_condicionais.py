MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar a CNH")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer apenas aulas teóricas!")

else:
        print("Ainda não pode tirar a CNH!")



