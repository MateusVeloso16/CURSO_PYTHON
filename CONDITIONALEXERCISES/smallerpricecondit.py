orcamento_1 = float(input("Qual o preco da empresa A? "))
orcamento_2 = float(input("Qual o preco da empresa B? "))
orcamento_3 = float(input("Qual o preco da empresa C? "))

if orcamento_1 > orcamento_2 and orcamento_1 > orcamento_3:
    maior_orcamento = orcamento_1
    if orcamento_2 > orcamento_3:
        menor_orcamento = orcamento_3
elif orcamento_2 > orcamento_1 and orcamento_2 > orcamento_3:
    maior_orcamento = orcamento_2
    if orcamento_1 > orcamento_3:
        menor_orcamento = orcamento_3
elif orcamento_3 > orcamento_1 and orcamento_3 > orcamento_2:
    maior_orcamento = orcamento_3
    if orcamento_2 > orcamento_1:
        menor_orcamento = orcamento_1
else:
    print("Something wrong. Please try again.")

print(f"O maior orcamento e: {maior_orcamento} e o menor orcamento e: {menor_orcamento}")