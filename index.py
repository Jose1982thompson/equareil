import flet as ft
import matplotlib.pyplot as plt
import numpy as np

# Variáveis globais
etapa = 1
acertos = 0
erros = 0

# Respostas esperadas (defina as suas respostas corretas)
resp_esp1 = ["resposta correta 1"]  # Adicione as respostas corretas
resp_esp2 = ["resposta correta 2"]  # Adicione as respostas corretas
resp_esp3 = ["resposta correta 3"]  # Adicione as respostas corretas
resp_esp4 = ["resposta correta 4"]  # Adicione as respostas corretas
resp_esp5 = ["resposta correta 5"]  # Adicione as respostas corretas

# Função para mostrar aviso
def mostrar_aviso(mensagem, dica=""):
    return ft.AlertDialog(
        title="Atenção",
        content=ft.Column(
            [
                ft.Text(mensagem, size=20),
                ft.Text(dica, size=16) if dica else None,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        actions=[ft.TextButton("OK", on_click=lambda _: av.view.remove(aviso_dialog))],
    )

# Função para mostrar sucesso
def mostrar_sucesso(mensagem):
    return ft.AlertDialog(
        title="Sucesso",
        content=ft.Text(mensagem, size=20),
        actions=[ft.TextButton("OK", on_click=lambda _: av.view.remove(sucesso_dialog))],
    )

# Função para calcular e verificar as respostas
def calcular(e):
    global etapa, erros, acertos
    resposta_usuario = e.control.value.strip().lower()
    
    if etapa == 1:
        if resposta_usuario in [resp.lower() for resp in resp_esp5]:
            acertos += 1
            etapa += 1
            av.view.add(mostrar_sucesso("Você acertou a primeira etapa!"))
        else:
            erros += 1
            av.view.add(mostrar_aviso("Sua resposta não está correta, tente novamente.",
                                       "Dica: reescreva a equação substituindo o valor de x e efetue as operações."))
    # Adicione as outras etapas da mesma forma...

    # Exiba a próxima pergunta
    mostrar_proxima_pergunta()

# Função para mostrar perguntas subsequentes
def mostrar_proxima_pergunta():
    av.view.remove_all()
    av.view.add(ft.Column([perguntas[etapa - 1]]))  # Adicione perguntas em uma lista

# Função para criar o gráfico
def mostrar_grafico():
    global acertos, erros
    
    # Criando gráfico
    plt.bar(['Acertos', 'Erros'], [acertos, erros])
    plt.ylabel('Número de Respostas')
    plt.title('Resultados')
    plt.show()

# Função principal para criar a interface
def main(page):
    global av
    av = page

    # Estruturas para perguntas e respostas
    global perguntas
    perguntas = [
        ft.Column([ft.Text("Pergunta 1"), ft.TextField(on_submit=calcular)]),
        ft.Column([ft.Text("Pergunta 2"), ft.TextField(on_submit=calcular)]),
        # Adicione as perguntas restantes...
    ]
    
    # Adiciona a primeira pergunta ao layout
    av.view.add(perguntas[0])

# Inicia a aplicação
ft.app(target=main)

