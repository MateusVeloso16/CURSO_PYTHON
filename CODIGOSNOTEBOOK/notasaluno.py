primeira_nota = float(input("Favor inserir a primeira nota do aluno: "))
segunda_nota = float(input("Favor inserir a segunda nota do aluno: "))
terceira_nota = float(input("Favor inserir a terceira nota do aluno: "))

media_nota = (primeira_nota + segunda_nota + terceira_nota) / 3

if media_nota >= 7 and media_nota < 10:
    print(f"Aprovado com a media de {media_nota:.3f} pontos.")
elif media_nota < 7:
    print(f"Reprovado com a media de {media_nota:.3f} pontos")
elif media_nota == 10:
    print(f"Aprovado com distincao com {media_nota:.3f} pontos")