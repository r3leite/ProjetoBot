from datetime import datetime
from io import BytesIO
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk

import requests
from PIL import Image, ImageTk

# Importando a função principal
from filmes.main import suggest_movies




# Cores ------------------------
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   #
co6 = "#03091f"   # azul

# Criando janela -----------------------------------------------------

janela = Tk()
janela.title("")
janela.geometry('460x560')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames -----------------------------------------------------

frameCima = Frame(janela, width=450, height=50, bg=co6,  relief="flat",)
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=60, bg=co1,  relief="solid",)
framePergunta.grid(row=1, column=0,padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=co1,  relief="solid",)
frameMeio.grid(row=2, column=0,padx=5, sticky=NSEW)

frameBaixo = Frame(janela,width=300, height=460,bg=co1, relief="raised")
frameBaixo.grid(row=3, column=0,  sticky=NSEW)


# Logo -----------------------------------------------------------------

# abrindo imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_nome = Label(frameCima, text='O chatbot de recomendação de filmes', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
app_nome.place(x=50, y=7)

l_linha = Label(frameCima, width=450,height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

# Pergunta -----------------------------------------------------------------

app_ = Label(framePergunta, text='Olá! Sou um chatbot de sugestões de filmes. Como você está se sentindo hoje?', width=45, height=2, wraplength=320, justify='center', compound=CENTER, padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'), bg=co1, fg=co0)
app_.place(x=0, y=7)

l_linha = Label(framePergunta, width=450,height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
l_linha.place(x=0, y=57)

# Funcao Resultado
def resultado(i):
    global capa_1, capa_2, capa_3

    # Filmes Sugeridos
    sugeridos = suggest_movies(i)

    titulos = sugeridos[0]
    poster = sugeridos[1]
    data = sugeridos[2]
    votos = sugeridos[3]

    #Limpando o frame baixo
    for widget in frameBaixo.winfo_children():
        widget.destroy()

    #---------------------------------------- Criando Frame para cada filme ------------------------------------
    # Filme 1
    frame_1 = Frame(frameBaixo, width=150, height=400, bg=co1)
    frame_1.grid(row=0, column=0, sticky=NSEW, pady=5)

    # Nome
    nome = Label(frame_1, text=f'{titulos[0]}', width=17, height=2, padx=10, pady=5, wraplength=100, justify='left', relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=7, y=260)

    # Data
    data_string_1 = f'{data[0]}'
    data_1 = datetime.strptime(data_string_1, '%Y-%m-%d')
    data_formatada = data_1.strftime('%B %Y')

    l_data_1 = Label(frame_1, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_data_1.place(x=5, y=310)

    # Voto
    l_voto_1 = Label(frame_1, text=f'Média de votos: {votos[0]}/10', anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_voto_1.place(x=5, y=330)

    # Obtendo a imagem

    # Obter o url da imagem a partir da API
    response_1 = requests.get(f'{poster[0]}')
    imagem_url_1 = response_1.url

    # carregando a imagem
    response_1 = requests.get(imagem_url_1)
    img_1 = Image.open(BytesIO(response_1.content))

    capa_1 = img_1
    capa_1 = capa_1.resize((150,250))
    capa_1 = ImageTk.PhotoImage(capa_1)

    l_capa_1 = Label(frame_1, image=capa_1, padx=5, bg=co1, fg=co0)
    l_capa_1.place(x=5, y=0)
# ------------------------------------------------------------------------------------------------------------------
# Filme 2
    frame_2 = Frame(frameBaixo, width=150, height=400, bg=co1)
    frame_2.grid(row=0, column=1, sticky=NSEW, pady=5)

    # Nome
    nome = Label(frame_2, text=f'{titulos[1]}', width=17, height=2, padx=10, pady=5, wraplength=100, justify='left', relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=7, y=260)

    # Data
    data_string_2 = f'{data[1]}'
    data_2 = datetime.strptime(data_string_2, '%Y-%m-%d')
    data_formatada = data_2.strftime('%B %Y')

    l_data_2 = Label(frame_2, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_data_2.place(x=5, y=310)

    # Voto
    l_voto_2 = Label(frame_2, text=f'Média de votos: {votos[1]}/10', anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_voto_2.place(x=5, y=330)

    # Obtendo a imagem

    # Obter o url da imagem a partir da API
    response_2 = requests.get(f'{poster[1]}')
    imagem_url_2 = response_2.url

    # carregando a imagem
    response_2 = requests.get(imagem_url_2)
    img_2 = Image.open(BytesIO(response_2.content))

    capa_2 = img_2
    capa_2 = capa_2.resize((150,250))
    capa_2 = ImageTk.PhotoImage(capa_2)

    l_capa_2 = Label(frame_2, image=capa_2, padx=5, bg=co1, fg=co0)
    l_capa_2.place(x=5, y=0)
#------------------------------------------------------------------------------------------------------------------------------
# Filme 3
    frame_3 = Frame(frameBaixo, width=150, height=400, bg=co1)
    frame_3.grid(row=0, column=2, sticky=NSEW, pady=5)

    # Nome
    nome = Label(frame_3, text=f'{titulos[2]}', width=17, height=2, padx=10, pady=5, wraplength=100, justify='left', relief=SOLID, anchor=NW, font=('Ivy 9 bold'), bg=co1, fg=co0, bd=1, highlightbackground='white')
    nome.place(x=7, y=260)

    # Data
    data_string_3 = f'{data[2]}'
    data_3 = datetime.strptime(data_string_3, '%Y-%m-%d')
    data_formatada = data_3.strftime('%B %Y')

    l_data_3 = Label(frame_3, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_data_3.place(x=5, y=310)

    # Voto
    l_voto_3 = Label(frame_3, text=f'Média de votos: {votos[2]}/10', anchor=NW, font=('Ivy 8'), bg=co1, fg=co0)
    l_voto_3.place(x=5, y=330)

    # Obtendo a imagem

    # Obter o url da imagem a partir da API
    response_3 = requests.get(f'{poster[2]}')
    imagem_url_3 = response_3.url

    # carregando a imagem
    response_3 = requests.get(imagem_url_3)
    img_3 = Image.open(BytesIO(response_3.content))

    capa_3 = img_3
    capa_3 = capa_3.resize((150,250))
    capa_3 = ImageTk.PhotoImage(capa_3)

    l_capa_3 = Label(frame_3, image=capa_3, padx=5, bg=co1, fg=co0)
    l_capa_3.place(x=5, y=0)








# Frame Meio ------------------------------------------------------------------------

#Configurando Botoes
img_1 = Image.open('image/anger.png')
img_1 = img_1.resize((28,28))
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frameMeio, command=lambda:resultado('Anger'), image=img_1, compound=LEFT, width=100, text=' Anger', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_1.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)

img_2 = Image.open('image/happy.png')
img_2 = img_2.resize((28,28))
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frameMeio, command=lambda:resultado('Happy'), image=img_2, compound=LEFT, width=100, text=' Happy', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_2.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)

img_3 = Image.open('image/ansiedade.png')
img_3 = img_3.resize((28,28))
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frameMeio, command=lambda:resultado('Ansiety'),image=img_3, compound=LEFT, width=100, text=' Ansiedade', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_3.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)

img_4 = Image.open('image/frustracao.png')
img_4 = img_4.resize((28,28))
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frameMeio, command=lambda:resultado('Frustration'),image=img_4, compound=LEFT, width=100, text=' Frustração', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_4.grid(row=0, column=3, sticky=NSEW, pady=2, padx=2)

img_5 = Image.open('image/gratidao.png')
img_5 = img_5.resize((28,28))
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frameMeio, command=lambda:resultado('Gratitude'),image=img_5, compound=LEFT, width=100, text=' Gratidão', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_5.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)

img_6 = Image.open('image/horror.png')
img_6 = img_6.resize((28,28))
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frameMeio, command=lambda:resultado('Horror'),image=img_6, compound=LEFT, width=100, text=' Horror', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_6.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2)

img_7 = Image.open('image/ok.png')
img_7 = img_7.resize((28,28))
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frameMeio, command=lambda:resultado('Ok'),image=img_7, compound=LEFT, width=100, text=' Ok', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_7.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2)

img_8 = Image.open('image/prazer.png')
img_8 = img_8.resize((28,28))
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frameMeio, command=lambda:resultado('Prazer'),image=img_8, compound=LEFT, width=100, text=' Prazer', bg=co1, fg=co0, font=('Ivy 10'), overrelief=RIDGE)
b_8.grid(row=1, column=3, sticky=NSEW, pady=2, padx=2)

janela.mainloop()