
print("Responda as perguntas abaixo com Sim ou Nao.")
tel_vitima = str(input("Voce telefonou para a vitima? "))
local_crime = str(input("Voce esteve no local do crime? "))
endereco_vitima = str(input("Voce mora perto da vitima? "))
dever_vitima = str(input("Voce devia dinheiro a vitima? "))
trabalho_vitima = str(input("Voce trabalhava com a vitima? "))

crime_count = 0

if "SIM" in tel_vitima.upper():
    crime_count = crime_count + 1
if "SIM" in local_crime.upper():
    crime_count = crime_count + 1 
if "SIM" in endereco_vitima.upper():
    crime_count = crime_count + 1 
if "SIM" in dever_vitima.upper():
    crime_count = crime_count + 1 
if "SIM" in trabalho_vitima.upper():
    crime_count = crime_count + 1 

if crime_count == 2:
    print("Suspeita")
elif crime_count > 2 and crime_count <= 4:
    print("Cumplice")
elif crime_count == 5:
    print("Assassino")
else:
    print("Inocente")