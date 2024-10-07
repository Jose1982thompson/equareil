import flet as ft
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

# Variáveis globais
etapa = 1
erros = 0
acertos = 0

# Respostas esperadas
resp_esp1 = ["3x+24=-x+4", "3x+24=4-x", "-x+4=3x+24", "-x+4=24+3x", "4-x=24+3x", "4-x=3x+24", "24+3x=-x+4", "24+3x=4-x"]
resp_esp2 = ["4x=-20", "-20=4x", "3x+x=4-24", "24-4=-x-3x"]
resp_esp3 = ["x=-5", "x = -5", "-5"]
resp_esp4 = ["y=9", "y = 9", "9"]
resp_esp5 = ["y=7", "7", "y = 7", "y=2*2+3", "y = 2*2 + 3", "y=4+3", "y = 4 + 3"]
resp_esp6 = ["8=2x+2", "2x=6", "6=2x", "2x = 6", "6 = 2x"]

# Função para mostrar mensagens
def mostrar_mensagem(msg, tipo="info"):
    if tipo == "success":
        return ft.AlertDialog(title="Sucesso", content=ft.Text(msg), actions=[ft.ElevatedButton("OK")]).show()
    elif tipo == "warning":
        return ft.AlertDialog(title="Atenção", content=ft.Text(msg), actions=[ft.ElevatedButton("OK")]).show()

# Função para calcular e verificar as respostas
def calcular(e):
    global etapa, erros, acertos
    resposta_usuario = ""

    if etapa == 1:
        resposta_usuario = resposta_5.value.strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp5]:
            acertos += 1
            mostrar_mensagem("Você acertou a primeira etapa!", "success")
            etapa += 1
            mostrar_proxima_pergunta()
        else:
            erros += 1
            mostrar_mensagem("Sua resposta não está correta, tente novamente.", "warning")

    # Adicione as verificações para as demais etapas seguindo o mesmo padrão

    # Aqui você pode continuar o código para outras etapas

# Função para mostrar a próxima pergunta
def mostrar_proxima_pergunta():
    global etapa
    if etapa == 2:
        pergunta_6.visible = True
        resposta_6.visible = True
        verificar_button_6.visible = True
    # Continue adicionando condições para as outras etapas

# Criar a interface
def main(page):
    global resposta_5, resposta_6, pergunta_6, verificar_button_6

    page.title = "Tutor de Matemática"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Página de Boas-vindas
    welcome_label = ft.Text("Bem-vindo ao Tutor de Matemática!", style="headlineMedium")
    instructions_label = ft.Text("Este tutorial irá guiá-lo através de várias etapas para resolver equações e sistemas de equações.", style="bodyMedium")
    start_button = ft.ElevatedButton("Começar", on_click=lambda e: mudar_pagina(2))

    page.add(welcome_label, instructions_label, start_button)

    # Página das Perguntas
    pergunta_5 = ft.Text("1) Encontre o valor de y fazendo a substituição necessária. Dada a reta y = 2x + 3, qual o valor de y quando x = 2")
    resposta_5 = ft.TextField(label="Resposta")
    verificar_button_5 = ft.ElevatedButton("Verificar", on_click=calcular)

    # Adicione as outras perguntas e entradas conforme necessário

    # Inicialmente, esconda as perguntas
    pergunta_6.visible = False
    resposta_6.visible = False
    verificar_button_6.visible = False

    # Exibir a página inicial
    page.add(pergunta_5, resposta_5, verificar_button_5)

# Iniciar o aplicativo
ft.app(target=main)
