def saudacao(nome):
    import random

    frases = ["bom dia! Meu nome é",
    "oi, tudo bem?"]
    print(frases[ramdom.randint(0,2)])
    
    def recebeTexto():
        texto = "Cliente: " + input("Cliente: ")
        palavraProibida = ["bocó"]
        for p in palavraProibida:
            if p in texto:
                print("Não vem não! Me respeite!")
                return recebeTexto()
            return texto

def buscaRespota(nome, texto):
    with open("BaseDeConhecimento.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ", "") == "tchau":
                    print(nome+ ": volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                print("Me desculpe, não sei o que falar")
                conhecimento.write("\n" + texto)
                resposta_user = input("O que esperava?\n")
                conhecimento.write("\n" + "Chatbot: " +
                resposta_user)
                return "Hum..."