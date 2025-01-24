primeiro_numero = float(input("Informe o primeiro numero: "))
segundo_numero = float(input("Informe o segundo numero: "))
terceiro_numero = float(input("Informe o terceiro numero: "))
maior_numero = 0
segmaior_numero = 0
menor_numero = 0


if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    maior_numero = primeiro_numero
    if segundo_numero > terceiro_numero:
        segmaior_numero = segundo_numero
        menor_numero = terceiro_numero
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    maior_numero = segundo_numero
    if primeiro_numero > terceiro_numero:
        segmaior_numero = primeiro_numero
        menor_numero = terceiro_numero
elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    maior_numero = terceiro_numero
    if primeiro_numero > segundo_numero:
        segmaior_numero = primeiro_numero
        menor_numero = segundo_numero
else:
    print("Something wrong.")

print(f"O maior numero e {maior_numero} seguido do segundo maior numero que e de {segmaior_numero} e depois o terceiro maior numero que e de {menor_numero}")