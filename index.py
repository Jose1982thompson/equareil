import tkinter as tk
from tkinter import messagebox

# Função para verificar as respostas
def calcular():
    global etapa
    if etapa == 2:
        resposta = resposta_6.get()
        if resposta == "algo esperável para resposta 6":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")
    elif etapa == 3:
        resposta = resposta_6b.get()
        if resposta == "algo esperável para resposta 6b":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")
    elif etapa == 4:
        resposta = resposta_6c.get()
        if resposta == "algo esperável para resposta 6c":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")
    elif etapa == 5:
        resposta = resposta_1.get()
        if resposta == "algo esperável para resposta 1":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")
    elif etapa == 6:
        resposta = resposta_2.get()
        if resposta == "algo esperável para resposta 2":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")
    elif etapa == 7:
        resposta = resposta_3.get()
        if resposta == "algo esperável para resposta 3":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")
    elif etapa == 8:
        resposta = resposta_4.get()
        if resposta == "algo esperável para resposta 4":  # Substitua pelo valor correto
            messagebox.showinfo("Correto", "Resposta correta!")
        else:
            messagebox.showerror("Errado", "Resposta errada, tente novamente.")

# Função para mudar de página
def mudar_pagina():
    global etapa
    etapa = 2
    frame_1.pack_forget()
    frame_2.pack()

# Função para exibir a próxima pergunta
def mostrar_proxima_pergunta():
    global etapa
    # Limpa a tela antes de exibir a próxima pergunta
    for widget in frame_2.winfo_children():
        widget.pack_forget()

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

# Configuração da janela principal
root = tk.Tk()
root.title("Quiz de Matemática")
root.geometry("800x600")

# Definindo frames
frame_1 = tk.Frame(root)
frame_2 = tk.Frame(root)

frame_1.pack()

# Adicionando elementos à página inicial (frame_1)
titulo = tk.Label(frame_1, text="Bem-vindo ao Quiz de Matemática!", font=("Arial", 24))
titulo.pack(pady=50)

instrucoes = tk.Label(frame_1, text="Clique no botão abaixo para começar", font=("Arial", 16))
instrucoes.pack(pady=20)

comecar_button = tk.Button(frame_1, text="Começar", command=mudar_pagina, font=("Arial", 16))
comecar_button.pack()

# Adicionando perguntas e entradas no frame_2
pergunta_6 = tk.Label(frame_2, text="Substitua o valor de y = 4 em g(y) = 2x + 2", font=("Arial", 16))
resposta_6 = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_6 = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_6b = tk.Label(frame_2, text="Isole x na equação resultante", font=("Arial", 16))
resposta_6b = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_6b = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_6c = tk.Label(frame_2, text="Resolva para x", font=("Arial", 16))
resposta_6c = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_6c = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_1 = tk.Label(frame_2, text="Pergunta 1: Qual é a resposta?", font=("Arial", 16))
resposta_1 = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_1 = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_2 = tk.Label(frame_2, text="Pergunta 2: Qual é a resposta?", font=("Arial", 16))
resposta_2 = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_2 = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_3 = tk.Label(frame_2, text="Pergunta 3: Qual é a resposta?", font=("Arial", 16))
resposta_3 = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_3 = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

pergunta_4 = tk.Label(frame_2, text="Pergunta 4: Qual é a resposta?", font=("Arial", 16))
resposta_4 = tk.Entry(frame_2, font=("Arial", 14))
verificar_button_4 = tk.Button(frame_2, text="Verificar", command=calcular, font=("Arial", 14))

# Inicializando a etapa
etapa = 0

# Iniciar o loop principal
root.mainloop()


