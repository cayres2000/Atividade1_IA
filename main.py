from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

def complmento(resposta,intencao):
    if intencao[0]['intent']=="entrega":
        pergunta = input("Deseja também saber mais sobre como começar seu tcc?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        if intencao[0]['intent']=="confirmacao":
            print("Assistente: "+resposta)
            resposta, intencao = myChatBot.chatbot_response("Como posso começar o tcc?")
            print("Assistente: "+resposta)
        else:
            print("Assistente: "+resposta)

#myChatBot.createModel()

print("Bem vindo ao Chatbot")

pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print("Assistente: "+resposta)
complmento(resposta, intencao)

while (intencao[0]['intent']!="despedida"):
    pergunta = input("Posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print("Assistente: "+resposta)
    complmento(resposta, intencao)

print("Foi um prazer atendê-lo")