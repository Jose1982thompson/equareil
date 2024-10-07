import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para centralizar a janela na tela
def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Função para criar uma janela de aviso personalizada
def mostrar_aviso(mensagem, dica=""):
    aviso_janela = tk.Toplevel(root)
    aviso_janela.title("Atenção")
    
    # Configurando a janela de aviso
    largura = 400
    altura = 200
    centralizar_janela(aviso_janela, largura, altura)
    aviso_janela.configure(bg="lightyellow")

    # Texto da mensagem com fonte maior
    label_aviso = tk.Label(aviso_janela, text=mensagem, font=("Arial", 16), bg="lightyellow", fg="orange", wraplength=350)
    label_aviso.pack(pady=10)

    # Texto da dica, se houver
    if dica:
        label_dica = tk.Label(aviso_janela, text=dica, font=("Arial", 14), bg="lightyellow", wraplength=350)
        label_dica.pack(pady=10)

    # Botão OK para fechar a janela
    botao_ok = tk.Button(aviso_janela, text="OK", command=aviso_janela.destroy, font=("Arial", 14), bg="red", fg="white")
    botao_ok.pack(pady=10)

# Função para criar uma janela de sucesso personalizada
def mostrar_sucesso(mensagem):
    sucesso_janela = tk.Toplevel(root)
    sucesso_janela.title("Sucesso")

    # Configurando a janela de sucesso
    largura = 400
    altura = 200
    centralizar_janela(sucesso_janela, largura, altura)
    sucesso_janela.configure(bg="lightgreen")

    # Texto da mensagem com fonte maior
    label_sucesso = tk.Label(sucesso_janela, text=mensagem, font=("Arial", 16), bg="lightgreen", fg="green", wraplength=350)
    label_sucesso.pack(pady=20)

    # Botão OK para fechar a janela
    botao_ok = tk.Button(sucesso_janela, text="OK", command=sucesso_janela.destroy, font=("Arial", 14), bg="green", fg="white")
    botao_ok.pack(pady=10)

# Função para calcular e verificar as respostas
def calcular():
    global etapa, erros, acertos
    resposta_usuario = ""

    if etapa == 1:
        resposta_usuario = resposta_5.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp5]:
            mostrar_sucesso("Você acertou a primeira etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", "Dica: reescreva a equação substituindo o valor de x e efetue as operações.")
            erros += 1
    elif etapa == 2:
        resposta_usuario = resposta_6.get().strip().lower()
        if resposta_usuario == "8=2x+2":
            mostrar_sucesso("Você acertou a segunda etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", "Dica: reescreva a equação substituindo o valor de y.")
            erros += 1
    elif etapa == 3:
        resposta_usuario = resposta_6b.get().strip().lower()
        if resposta_usuario in ["2x=6", "6=2x"]:
            mostrar_sucesso("Você acertou a terceira etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", "Dica: subtraia 2 nos dois lados da equação.")
            erros += 1
    elif etapa == 4:
        resposta_usuario = resposta_6c.get().strip().lower()
        if resposta_usuario in ["x=3", "3"]:
            mostrar_sucesso("Você acertou a quarta etapa!")
            acertos += 1
            etapa += 1
            mudar_pagina(3)
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", "Dica: divida por 2 nos dois lados da equação.")
            erros += 1
    elif etapa == 5:
        resposta_usuario = resposta_1.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp1]:
            mostrar_sucesso("Você acertou a quinta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", "Dica: iguale as equações das retas f e g.")
            erros += 1
    elif etapa == 6:
        resposta_usuario = resposta_2.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp2]:
            mostrar_sucesso("Você acertou a sexta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", "Dica: Isole o X em um dos lados da equação.")
            erros += 1
    elif etapa == 7:
        resposta_usuario = resposta_3.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp3]:
            mostrar_sucesso("Você acertou a sétima etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            mostrar_aviso("Atenção", "Sua resposta não está correta, tente novamente. \nDica: Divida ambos os membros da equação por 4.")
            erros += 1
    elif etapa == 8:
        resposta_usuario = resposta_4.get().strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp4]:
            mostrar_sucesso("Sucesso: Você acertou todas as etapas!\n\nO ponto de interseção das retas f e g é  x = -5 e y = 9")
            acertos += 1
            etapa += 1
            root.after(100, lambda: mudar_pagina(8))
        else:
            mostrar_aviso("Atenção", "Sua resposta não está correta, tente novamente.\nDica: substitua o valor de X em alguma das equações f ou g.")
            erros += 1

# Função para mostrar as perguntas subsequentes na mesma página
def mostrar_proxima_pergunta():
    global etapa
    if etapa == 2:
        pergunta_6.pack(pady=20)
        resposta_6.pack()
        verificar_button_6.pack(pady=3)
    elif etapa == 3:
        pergunta_6b.pack(pady=20)
        resposta_6b.pack()
        verificar_button_6b.pack(pady=3)
    elif etapa == 4:
        pergunta_6c.pack(pady=20)
        resposta_6c.pack()
        verificar_button_6c.pack(pady=3)
    elif etapa == 5:
        pergunta_1.pack(pady=20)
        resposta_1.pack()
        verificar_button_1.pack(pady=3)
    elif etapa == 6:
        pergunta_2.pack(pady=20)
        resposta_2.pack()
        verificar_button_2.pack(pady=3)      
    elif etapa == 7:
        pergunta_3.pack(pady=20)
        resposta_3.pack()
        verificar_button_3.pack(pady=3)
    elif etapa == 8:
        pergunta_4.pack(pady=20)
        resposta_4.pack()
        verificar_button_4.pack(pady=3)

# Função para mudar de página
def mudar_pagina(pagina):
    frame_welcome.pack_forget()
    frame_1.pack_forget()
    frame_2.pack_forget()
    frame_results.pack_forget()

    if pagina == 1:
        frame_welcome.pack(fill="both", expand=1)
    elif pagina == 2:
        frame_1.pack(fill="both", expand=1)
    elif pagina == 3:
        frame_2.pack(fill="both", expand=1)
    elif pagina == 8:
        frame_results.pack(fill="both", expand=1)
        mostrar_grafico()

# Função para mostrar resultados gráficos
def mostrar_grafico():
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.bar(['Erros', 'Acertos'], [erros, acertos], color=['red', 'green'])
    ax.set_title("Resultados da avaliação")
    ax.set_xlabel("Tipo")
    ax.set_ylabel("Quantidade")

    canvas = FigureCanvasTkAgg(fig, master=frame_results)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=50)

# Configurações iniciais
root = tk.Tk()
root.title("Sistema Tutorial")
root.geometry("800x600")
centralizar_janela(root, 800, 600)

frame_welcome = tk.Frame(root)
frame_1 = tk.Frame(root)
frame_2 = tk.Frame(root)
frame_results = tk.Frame(root)

for frame in (frame_welcome, frame_1, frame_2, frame_results):
    frame.grid(row=0, column=0, sticky="nsew")

# Variáveis globais
etapa = 1
acertos = 0
erros = 0

# Respostas esperadas para diferentes etapas
resp_esp1 = ["3x + 1 = 4x - 5", "-5 = 4x - 3x + 1"]
resp_esp2 = ["-5 = x + 1"]
resp_esp3 = ["x = -6"]
resp_esp4 = ["y = 9"]
resp_esp5 = ["7 = 2(3)+1"]

# Página de boas-vindas
label_welcome = tk.Label(frame_welcome, text="Bem-vindo ao sistema tutorial", font=("Arial", 18))
label_welcome.pack(pady=30)

iniciar_button = tk.Button(frame_welcome, text="Iniciar", command=lambda: mudar_pagina(2), font=("Arial", 14))
iniciar_button.pack(pady=20)

# Frame 1 - Primeira Pergunta
pergunta_5 = tk.Label(frame_1, text="Substitua o valor de x = 3 em f(x) = 2x + 1", font=("Arial", 16))
resposta_5 = tk.Entry(frame_1, font=("Arial", 14))
verificar_button_5 = tk.Button(frame_1, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_5.pack(pady=20)
resposta_5.pack()
verificar_button_5.pack(pady=3)

# Frame 2 - Segunda Pergunta
pergunta_6 = tk.Label(frame_2, text="Substitua o valor de y = 4 em g(y) = 2x + 2", font=("Arial", 16))
resposta_6 = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_6 = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_6b = tk.Label(frame_2, text="Isole x na equação resultante", font=("Arial", 16))
resposta_6b = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_6b = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_6c = tk.Label(frame_2, text="Resolva para x", font=("Arial", 16))
resposta_6c = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_6c = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

# Frame 3 - Resultados
label_results = tk.Label(frame_results, text="Resultados", font=("Arial", 18))
label_results.pack(pady=30)

# Iniciar no frame de boas-vindas
mudar_pagina(1)
root.mainloop()

