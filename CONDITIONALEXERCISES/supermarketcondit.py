tipo_carne = int(input("Qual o tipo de carne voce vai levar? Digite 1 para File Duplo, 2 para Alcatra e 3 para Picanha."))

quilos_carne = float(input("Quantos quilos de carne voce vai levar? "))

tipo_pagamento = str(input("Qual o tipo de pagamento: Digite C para cartao tabajara e D para dinheiro."))

if tipo_carne == 1:
    name_carne = "File"
elif tipo_carne == 2:
    name_carne = "Alcatra"
elif tipo_carne == 3:
    name_carne = "Picanha"

if tipo_pagamento == "C":
    name_pagamento = "Cartao Tabajara"
elif tipo_pagamento == "D":
    name_pagamento = "Dinheiro"

if tipo_carne == 1: #File Duplo
    if quilos_carne <= 5:
        preco_total = quilos_carne * 4.9
    else:
        preco_total = quilos_carne * 5.8
elif tipo_carne == 2: #Alcatra
    if quilos_carne <= 5:
        preco_total = quilos_carne * 5.9
    else:
        preco_total = quilos_carne * 6.8
elif tipo_carne == 3: #Picanha
    if quilos_carne <= 5:
        preco_total = quilos_carne * 6.9
    else:
        preco_total = quilos_carne * 7.8

if tipo_pagamento == "C":
    valor_desconto = preco_total * 0.05
    valor_a_pagar = preco_total - valor_desconto
else:
    valor_a_pagar = preco_total

print(f"Tipo de carne: {name_carne}")
print(f"Quantidade de carne: {quilos_carne:.1f}Kg")
print(f"O preco total da carne foi de R$:{preco_total:.2f}")
print(f"O tipo de pagamento foi: {name_pagamento}")
print(f"O valor do desconto foi de R$:{valor_desconto:.2f}")
print(f"O valor total a pagar e R$:{valor_a_pagar:.2f}")

print("Volte sempre..")