orcamento_1 = float(input("Qual o seu preco da empresa A? "))
orcamento_2 = float(input("Qual o preco da empresa B? "))
orcamento_3 = float(input("Qual o preco da empresa C? "))

if orcamento_1 > orcamento_2 and orcamento_1 > orcamento_3:
    print("Orcamento 1 e o mais caro.")
elif orcamento_2 > orcamento_1 and orcamento_2 > orcamento_3:
    print("Orcamento 2 e o mais caro.")
elif orcamento_3 > orcamento_1 and orcamento_3 > orcamento_2:
    print("Orcamento 3 e o mais caro.")
else:
    print("Something wrong. Please try again.")