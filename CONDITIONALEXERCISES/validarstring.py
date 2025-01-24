numero_telefone = input("Informe o numero de telefone: ")
print(numero_telefone)


numero_telefone = numero_telefone.strip()
print(numero_telefone)

len_telefone = len(numero_telefone)

if len_telefone == 7:
    numero_telefone = "3" + numero_telefone
    print(numero_telefone)
elif len_telefone == 8:
    print("Numero digitado corretamente. ")
else:
    print("Numero invalido. Tente novamente. ")