string_1 = input("Favor informar a primeira string: ")
string_2 = input("Favor informar a segunda string: ")


print(string_1)
print(len(string_1))
print(string_2)
print(len(string_2))

if (len(string_1)) == (len(string_2)):
    print("A string 1 e a string 2 tem o mesmo comprimento. ")
else:
    print("A string 1 e a string 2 NAO tem o mesmo comprimento. ")

if string_1 == string_2:
    print("O conteudo da string 1 e da string 2 sao iguais. ")
else:
    print("O conteudo da string 1 e da string 2 NAO sao iguais. ")