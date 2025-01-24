numero_telefone = input("Informe o numero de telefone: ")


numero_telefone = numero_telefone.strip()

len_telefone = len(numero_telefone)

if "-" in numero_telefone:
    numero_telefone = numero_telefone.replace("-", (""))

if len_telefone == 7:
    numero_telefone = "3" + numero_telefone
elif len_telefone == 8:
    print("Numero digitado corretamente. ")
else:
    print("Numero invalido. Tente novamente. ")

print(numero_telefone)