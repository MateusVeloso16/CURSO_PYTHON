peso_maximo = 50
multa_excedente = 4
peso_peixe = float(input("Favor informar o peso do peixe: "))

if peso_peixe > 50:
    peso_excedente = peso_peixe - peso_maximo
    multa_peixe = peso_excedente * multa_excedente
    print(f"O peso excedente do peixe foi de {peso_excedente}Kg e a multa que devera pagar e de {multa_peixe:.2f} reais")
else:
    print("O peso do peixe esta dentro do permitido. Voce nao precisa pagar multa.")