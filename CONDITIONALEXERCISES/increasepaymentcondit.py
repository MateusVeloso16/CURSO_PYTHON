salario = float(input("Favor informar o seu salario no seguinte formato 0000.00: "))
aumento_um = 1.2
aumento_dois = 1.5
aumento_tres = 1.1
aumento_quatro = 1.05

if salario <= 280:
    novo_salario = salario * aumento_um
    percentual_aumento = aumento_um
    qtd_aumento = novo_salario - salario
elif salario > 280 and salario < 700:
    novo_salario = salario * aumento_dois
    percentual_aumento = aumento_dois
    qtd_aumento = novo_salario - salario
elif salario >= 700 and salario < 1500:
    novo_salario = salario * aumento_tres
    percentual_aumento = aumento_tres
    qtd_aumento = novo_salario - salario
elif salario >= 1500:
    novo_salario = salario * aumento_quatro
    percentual_aumento = aumento_quatro
    qtd_aumento = novo_salario - salario
else:
    print("Something is wrong. Please try again.")

print(f"O salario antes do reajuste era de R$:{salario:.2f}")
print(f"O salario com o reajuste e de R$:{novo_salario:.2f}")
print(f"O percentual do aumento foi de {percentual_aumento}%")
print(f"O valor real do aumento foi de R$:{qtd_aumento:.2f}")

