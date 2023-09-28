import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"oi|Ola|hey|hello!",
        ["Ola", "Oi", "Hey!"]
    ],

    [
        r"Qual e o seu nome?",
        ["Meu nome é Chatbot", "Eu sou o Chatbot!"]
    ],

    [
        r"Como estas?| Como voce esta?|Como estas se sentindo?|Como vai?",
        ["Estou bem, obrigado! E voce?", "Estou otimo!", "Vou bem!"]
    ],

    [
        r"adeus|tchau|bye bye|bye",
        ["Tchau", "Até mais", "Até a próxima"]
    ],

]

def chatbot():
    print("Olá! sou o Chatbot. Como posso ajuda-lo hoje?")
    chat = Chat(pares, reflections)

    while True:
        try:
            resposta = chat.respond(input())
            print(resposta)

        except KeyboardInterrupt:
            break
chatbot()



