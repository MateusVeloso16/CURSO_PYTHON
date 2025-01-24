tipo_combustivel = str(input("Qual o tipo de combustivel abastecido? Escreva G para Gasolina ou A para Alcool."))

litros_combustivel = float(input("Quantos litros de combustivel foram abastecidos? "))

preco_gasolina = 2.5
preco_alcool = 1.9

#If Gasolina

if "G" in tipo_combustivel.upper():
    if litros_combustivel <= 20:
        custo_combustivel = (litros_combustivel * 2.5) - (litros_combustivel * 0.04)
    else:
        custo_combustivel = (litros_combustivel * 2.5) - (litros_combustivel * 0.06)
elif "A" in tipo_combustivel.upper():
    if litros_combustivel <= 20:
        custo_combustivel = (litros_combustivel * 1.9) - (litros_combustivel * 0.03)
    else:
        custo_combustivel = (litros_combustivel * 1.9) - (litros_combustivel * 0.05)
else:
    print("Something wrong. Please try again.")

print(f"O custo total de combustivel abastecido foi de R$:{custo_combustivel:.2f}")
