import flet as ft

# Variáveis globais
etapa = 1
acertos = 0
erros = 0

# Definindo as respostas esperadas
resp_esp1 = ["x=-5", "-5"]
resp_esp2 = ["y=9", "9"]
resp_esp3 = ["equação correta", "solução correta"]
resp_esp4 = ["interseção correta", "solução final"]
resp_esp5 = ["equação 1", "resposta esperada"]

# Função para criar uma janela de aviso personalizada
def mostrar_aviso(page, mensagem, dica=""):
    def fechar_aviso(e):
        page.dialog.open = False
        page.update()

    page.dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Atenção"),
        content=ft.Column(
            [
                ft.Text(mensagem, size=16, color="orange"),
                ft.Text(dica, size=14),
            ]
        ),
        actions=[ft.TextButton("OK", on_click=fechar_aviso)],
    )
    page.dialog.open = True
    page.update()

# Função para criar uma janela de sucesso personalizada
def mostrar_sucesso(page, mensagem):
    def fechar_sucesso(e):
        page.dialog.open = False
        page.update()

    page.dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sucesso"),
        content=ft.Text(mensagem, size=16, color="green"),
        actions=[ft.TextButton("OK", on_click=fechar_sucesso)],
    )
    page.dialog.open = True
    page.update()

# Função para verificar e calcular as respostas
def calcular(page):
    global etapa, acertos, erros
    if etapa == 1:
        resposta_usuario = resposta_5.value.strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp5]:
            mostrar_sucesso(page, "Você acertou a primeira etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Sua resposta não está correta, tente novamente.",
                          "Dica: reescreva a equação substituindo o valor de x e efetue as operações.")
            erros += 1
    elif etapa == 2:
        resposta_usuario = resposta_6.value.strip().lower()
        if resposta_usuario == "8=2x+2":
            mostrar_sucesso(page, "Você acertou a segunda etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Sua resposta não está correta, tente novamente.",
                          "Dica: reescreva a equação substituindo o valor de y.")
            erros += 1
    elif etapa == 3:
        resposta_usuario = resposta_6b.value.strip().lower()
        if resposta_usuario in ["2x=6", "6=2x"]:
            mostrar_sucesso(page, "Você acertou a terceira etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Sua resposta não está correta, tente novamente.",
                          "Dica: subtraia 2 nos dois lados da equação.")
            erros += 1
    elif etapa == 4:
        resposta_usuario = resposta_6c.value.strip().lower()
        if resposta_usuario in ["x=3", "3"]:
            mostrar_sucesso(page, "Você acertou a quarta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Sua resposta não está correta, tente novamente.",
                          "Dica: divida por 2 nos dois lados da equação.")
            erros += 1
    elif etapa == 5:
        resposta_usuario = resposta_1.value.strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp1]:
            mostrar_sucesso(page, "Você acertou a quinta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Sua resposta não está correta, tente novamente.",
                          "Dica: iguale as equações das retas f e g.")
            erros += 1
    elif etapa == 6:
        resposta_usuario = resposta_2.value.strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp2]:
            mostrar_sucesso(page, "Você acertou a sexta etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Sua resposta não está correta, tente novamente.",
                          "Dica: Isole o X em um dos lados da equação.")
            erros += 1
    elif etapa == 7:
        resposta_usuario = resposta_3.value.strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp3]:
            mostrar_sucesso(page, "Você acertou a sétima etapa!")
            acertos += 1
            etapa += 1
            mostrar_proxima_pergunta(page)
        else:
            mostrar_aviso(page, "Atenção", "Sua resposta não está correta, tente novamente. \\nDica: Divida ambos os membros da equação por 4.")
            erros += 1
    elif etapa == 8:
        resposta_usuario = resposta_4.value.strip().lower()
        if resposta_usuario in [resp.lower() for resp in resp_esp4]:
            mostrar_sucesso(page, "Sucesso: Você acertou todas as etapas! \\n \\nO ponto de interseção das retas f e g é  x = -5 e y = 9")
            acertos += 1
            etapa += 1
            page.go("/resultados")
        else:
            mostrar_aviso(page, "Atenção", "Sua resposta não está correta, tente novamente. \\nDica: substitua o valor de X em alguma das equações f ou g.")
            erros += 1

# Função para mostrar as próximas perguntas
def mostrar_proxima_pergunta(page):
    global etapa
    # Ocultar todas as perguntas
    pergunta_6.visible = False
    pergunta_6b.visible = False
    pergunta_6c.visible = False

    if etapa == 2:
        pergunta_6.visible = True
    elif etapa == 3:
        pergunta_6b.visible = True
    elif etapa == 4:
        pergunta_6c.visible = True

    page.update()  # Atualizar a página para refletir as mudanças

# Função para mudar de página
def mudar_pagina(page, pagina):
    if pagina == 1:
        page.go("/")

# Função principal do app
def main(page):
    global pergunta_6, pergunta_6b, pergunta_6c, resposta_1, resposta_2, resposta_3, resposta_4
    global resposta_5, resposta_6, resposta_6b, resposta_6c

    page.title = "Exercícios Interativos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    resposta_1 = ft.TextField(label="Resposta 1")
    resposta_2 = ft.TextField(label="Resposta 2")
    resposta_3 = ft.TextField(label="Resposta 3")
    resposta_4 = ft.TextField(label="Resposta 4")
    resposta_5 = ft.TextField(label="Resposta 5")
    resposta_6 = ft.TextField(label="Resposta 6")
    resposta_6b = ft.TextField(label="Resposta 6b")
    resposta_6c = ft.TextField(label="Resposta 6c")

    pergunta_6 = ft.Text("Pergunta 6", visible=False)
    pergunta_6b = ft.Text("Pergunta 6b", visible=False)
    pergunta_6c = ft.Text("Pergunta 6c", visible=False)

    page.add(
        ft.Column(
            [
                resposta_5,
                ft.ElevatedButton("Verificar Resposta", on_click=lambda e: calcular(page)),
                pergunta_6,
                resposta_6,
                pergunta_6b,
                resposta_6b,
                pergunta_6c,
                resposta_6c,
                resposta_1,
                resposta_2,
                resposta_3,
                resposta_4,
            ]
        )
    )

ft.app(target=main)
