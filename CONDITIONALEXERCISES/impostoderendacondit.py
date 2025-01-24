valor_hora = float(input("Qual o seu valor hora? "))
qtd_horas = float(input("Quantas horas voce trabalha no mes? "))

salario_bruto = valor_hora * qtd_horas
fgts_desconto = salario_bruto * 0.11
inss_desconto = salario_bruto * 0.1

#Desconto imposto de renda:

if salario_bruto <= 900:
    imposto_renda = 0
    percentual_ir = "0%"
elif salario_bruto > 900 and salario_bruto <= 1500:
    imposto_renda = 0.05
    percentual_ir = "5%"
elif salario_bruto > 1500 and salario_bruto <=2500:
    imposto_renda = 0.1
    percentual_ir = "10%"
elif salario_bruto > 2500:
    imposto_renda = 0.2
    percentual_ir = "20%"
else:
    print("Something wrong. Please try again.")

ir_desconto = salario_bruto * imposto_renda
total_descontos = inss_desconto + ir_desconto
salario_liquido = salario_bruto - total_descontos

print(f"Salario bruto: R$:{salario_bruto}")
print(f"(-) IR ({percentual_ir}): R$:{ir_desconto}")
print(f"(-) INSS (10%): R$:{inss_desconto}")
print(f"FGTS (11%): R$:{fgts_desconto}")
print(f"Total de descontos: R$:{total_descontos}")
print(f"Salario liquido: R$:{salario_liquido}")