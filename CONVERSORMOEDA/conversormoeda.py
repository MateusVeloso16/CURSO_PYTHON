import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

titulo = customtkinter.CTkLabel(janela, text = "Conversor de Moedas", font=("Arial",25))
texto_moeda_origem = customtkinter.CTkLabel(janela, text = "Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text = "Selecione a moeda de destino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"])

def converter_moeda():
    print("Converter moeda")
botao_converte = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD: Dolar Americano", "BRL: Real Brasileiro", "BTC: Bitcoin"]
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()


# moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dolar Americano")
# moeda2 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real Brasileiro")
# moeda3 = customtkinter.CTkLabel(lista_moedas, text="BTC: Bitcoin")
# moeda1.pack()
# moeda2.pack()
# moeda3.pack()


titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converte.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)


janela.mainloop()
