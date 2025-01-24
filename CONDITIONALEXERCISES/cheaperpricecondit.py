produto_um = float(input("Qual o preco do produto A? "))
produto_dois = float(input("Qual o preco do produto B? "))
produto_tres = float(input("Qual o preco do procuto C? "))

if produto_um < produto_dois and produto_um < produto_tres:
    mais_barato = produto_um
elif produto_dois < produto_um and produto_dois < produto_tres:
    mais_barato = produto_dois
elif produto_tres < produto_um and produto_tres < produto_dois:
    mais_barato = produto_tres
else:
    print("Alguma coisa errada. Por favor comece de novo.")

print(f"Voce deveria comprar o produto de valor R$:{mais_barato:.5f} porque e o produto mais barato.")