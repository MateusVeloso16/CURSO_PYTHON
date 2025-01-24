morango_comprado = float(input("Quantos quilos de morango foram comprados? "))
maca_comprado = float(input("Quantos quilos de maca foram comprados? "))

if morango_comprado <= 5:
    total_morango = morango_comprado * 2.5
else:
    total_morango = morango_comprado * 2.2

if maca_comprado <= 5:
    total_maca = maca_comprado * 1.8
else:
    total_maca = maca_comprado * 1.5

custo_total = total_maca + total_morango

if (morango_comprado + maca_comprado) >= 8 or custo_total >= 25:
    custo_total = custo_total - (custo_total * 0.1)

print(f"O custo total da compra foi de R$:{custo_total:.2f}")