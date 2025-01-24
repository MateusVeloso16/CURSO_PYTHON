area_metros = float(input("Qual o tamanho em metros da area a ser pintada em m2? "))

preco_18litros = 80
preco_3c6litros = 25

litros_necessarios = area_metros // 6
resto_necessario = area_metros % 6
if resto_necessario != 0:
    litros_necessarios = litros_necessarios + 1

tinta18_litros = litros_necessarios // 18
if litros_necessarios % 18 != 0:
    tinta18_litros = tinta18_litros + 1

tinta3c6litros = litros_necessarios // 3.6
if litros_necessarios % 3.6 != 0:
    tinta3c6litros = tinta3c6litros + 1

Tinta18_valor = tinta18_litros * preco_18litros
Tinta3c6_valor = tinta3c6litros * preco_3c6litros

#Sugestion to spend less money

print(f"Valor que vai pagar se levar apenas latas de 18 litros: R$:{Tinta18_valor}")
print(f"Valor que vai pagar se levar apenas latas de 3.6 litros: R$:{Tinta3c6_valor}")

print(f"O numero de Laoes de 18 litros que vai ter que levar para cobrir a area desejada: {tinta18_litros}")
print(f"O numero de Laoes de 3.6 litros que vai ter que levar para cobrir a area desejada: {tinta3c6litros}")
print(f"O numero total de litros de tinta necessarios para cobrir a area desejada {litros_necessarios}")
print(f"Essa e a quantidade de tinta que causa o arredondamento de litros para cima: {resto_necessario}")