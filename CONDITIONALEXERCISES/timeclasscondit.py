turno_aula = str(input("Em que turno você estuda? Favor digitar M-matutino ou V-Vespertino ou N- Noturno. "))
turno_aula = turno_aula.upper()

if turno_aula == "M":
    print("Bom dia!")
elif turno_aula == "V":
    print("Boa tarde!")
elif turno_aula == "N":
    print("Boa Noite!")
else:
    print("Valor invalido. Por favor tente de novo.")
