ano_numero = int(input("Informe o ano que quer saber se e um ano bisexto: "))

modulo_quatrocentos = ano_numero % 400
module_quatro = ano_numero % 4
module_cem = ano_numero % 100


if (module_quatro == 0 and (module_cem != 0 or modulo_quatrocentos == 0)):
    print("E um ano bissexto.")
else:
    print("Nao e um ano bissexto.")