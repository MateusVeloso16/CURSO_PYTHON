import xmltodict

def nomes_moedas():
    with open("CONVERSORMOEDA\moedas.xml", "rb") as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dic_moedas["xml"]
    return moedas

with open("CONVERSORMOEDA\conversoes.xml", "rb") as arquivo_conversoes:
    dic_conversoes = xmltodict.parse(arquivo_conversoes)

conversoes = dic_conversoes["xml"]
print(dic_conversoes)