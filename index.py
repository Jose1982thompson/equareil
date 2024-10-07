import flet as ft

# Variáveis globais
etapa = 1
erros = 0
acertos = 0
resp_esp1 = ["3x+24=-x+4", "3x+24=4-x", "-x+4=3x+24", "-x+4=24+3x", "4-x=24+3x", "4-x=3x+24", "24+3x=-x+4", "24+3x=4-x"]
resp_esp2 = ["4x=-20", "-20=4x", "3x+x=4-24", "24-4=-x-3x"]
resp_esp3 = ["x=-5", "x = -5", "-5"]
resp_esp4 = ["y=9", "y = 9", "9"]
resp_esp5 = ["y=7", "7", "y = 7", "y=2*2+3", "y = 2*2 + 3", "y=4+3", "y = 4 + 3"]
resp_esp6 = ["8=2x+2", "2x=6", "6=2x", "2x = 6", "6 = 2x"]

# Funções para exibir mensagens
def mostrar_aviso(mensagem, dica=""):
    return ft.alert(mensagem + (f"\nDica: {dica}" if dica else ""))

def mostrar_sucesso(mensagem):
    return ft.alert(mensagem)

def calcular(resposta_usuario, etapa_atual):
    global etapa, erros, acertos
    if etapa_atual == 1:
        if resposta_usuario.lower() in [resp.lower() for resp in resp_esp5]:
            mostrar_sucesso("Você acertou a primeira etapa!")
            acertos += 1
            etapa += 1
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: reescreva a equação substituindo o valor de x e efetue as operações.")
            erros += 1
    elif etapa_atual == 2:
        if resposta_usuario == "8=2x+2":
            mostrar_sucesso("Você acertou a segunda etapa!")
            acertos += 1
            etapa += 1
        else:
            mostrar_aviso("Sua resposta não está correta, tente novamente.", 
                          "Dica: reescreva a equação substituindo o valor de y.")
            erros += 1
    # Continue com as demais etapas...
    
    if etapa > 8:
        mostrar_sucesso("Sucesso: Você completou todas as etapas!")

# Função para gerenciar a interface
def main(page):
    global etapa
    page.title = "Tutor de Matemática"
    page.bgcolor = "lightgreen"

    def mudar_pagina(pagina):
        if pagina == 1:
            frame_welcome.visible = True
            frame_questions.visible = False
            frame_results.visible = False
        elif pagina == 2:
            frame_welcome.visible = False
            frame_questions.visible = True
            frame_results.visible = False
        elif pagina == 3:
            frame_welcome.visible = False
            frame_questions.visible = False
            frame_results.visible = True

    # Página de Boas-vindas
    frame_welcome = ft.Column(
        controls=[
            ft.Text("Bem-vindo ao Tutor de Matemática!", size=20),
            ft.Text("Este tutorial irá guiá-lo através de várias etapas para resolver equações."),
            ft.ElevatedButton("Começar", on_click=lambda _: mudar_pagina(2)),
        ],
        visible=True
    )

    # Página de Perguntas
    frame_questions = ft.Column(
        controls=[
            ft.Text("1) Encontre o valor de y fazendo a substituição necessária. "
                    "Dada a reta y = 2x + 3, qual o valor de y quando x = 2"),
            ft.TextField(on_submit=lambda e: calcular(e.control.value, 1)),
            ft.Text("2) Dada a reta y = 2x + 2, encontre o valor de x quando y = 8."),
            ft.TextField(on_submit=lambda e: calcular(e.control.value, 2)),
            # Adicione mais perguntas e campos conforme necessário
        ],
        visible=False
    )

    # Página de Resultados
    frame_results = ft.Column(
        controls=[
            ft.Text("Resultados:"),
            ft.Text(f"Corretas: {acertos}"),
            ft.Text(f"Erradas: {erros}"),
            # Adicione gráficos ou mais informações conforme necessário
        ],
        visible=False
    )

    # Adicionando os frames à página
    page.add(frame_welcome, frame_questions, frame_results)

ft.app(target=main)
