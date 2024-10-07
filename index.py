import flet as ft
import matplotlib.pyplot as plt
import numpy as np

# Variáveis globais
etapa = 1
acertos = 0
erros = 0

# Respostas esperadas (defina as suas respostas corretas)
resp_esp1 = ["1", "um", "1,0", "1.0"]
resp_esp2 = ["4", "quatro", "4,0", "4.0"]
resp_esp3 = ["6", "seis", "6,0", "6.0"]
resp_esp4 = ["7", "sete", "7,0", "7.0"]
resp_esp5 = ["10", "dez", "10,0", "10.0"]

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
        if resposta_usuario in [resp.lower() for resp in resp_esp1]:
            acertos += 1
            etapa += 1
            av.view.add(mostrar_sucesso("Você acertou a primeira etapa!"))
        else:
            erros += 1
            av.view.add(mostrar_aviso("Sua resposta não está correta, tente novamente.",
                                       "Dica: reescreva a equação substituindo o valor de x e efetue as operações."))

    elif etapa == 2:
        if resposta_usuario in [resp.lower() for resp in resp_esp2]:
            acertos += 1
            etapa += 1
            av.view.add(mostrar_sucesso("Você acertou a segunda etapa!"))
        else:
            erros += 1
            av.view.add(mostrar_aviso("Sua resposta não está correta, tente novamente.",
                                       "Dica: reescreva a equação substituindo o valor de x e efetue as operações."))

    elif etapa == 3:
        if resposta_usuario in [resp.lower() for resp in resp_esp3]:
            acertos += 1
            etapa += 1
            av.view.add(mostrar_sucesso("Você acertou a terceira etapa!"))
        else:
            erros += 1
            av.view.add(mostrar_aviso("Sua resposta não está correta, tente novamente.",
                                       "Dica: reescreva a equação substituindo o valor de x e efetue as operações."))

    elif etapa == 4:
        if resposta_usuario in [resp.lower() for resp in resp_esp4]:
            acertos += 1
            etapa += 1
            av.view.add(mostrar_sucesso("Você acertou a quarta etapa!"))
        else:
            erros += 1
            av.view.add(mostrar_aviso("Sua resposta não está correta, tente novamente.",
                                       "Dica: reescreva a equação substituindo o valor de x e efetue as operações."))

    elif etapa == 5:
        if resposta_usuario in [resp.lower() for resp in resp_esp5]:
            acertos += 1
            av.view.add(mostrar_sucesso("Você acertou a quinta etapa!"))
            mostrar_grafico()
        else:
            erros += 1
            av.view.add(mostrar_aviso("Sua resposta não está correta, tente novamente.",
                                       "Dica: reescreva a equação substituindo o valor de x e efetue as operações."))

    # Exiba a próxima pergunta
    mostrar_proxima_pergunta()

# Função para mostrar perguntas subsequentes
def mostrar_proxima_pergunta():
    av.view.remove_all()
    if etapa <= 5:
        av.view.add(perguntas[etapa - 1])  # Adiciona a próxima pergunta
    else:
        av.view.add(ft.Text("Parabéns! Você completou todas as etapas.", size=24))

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
        ft.Column([ft.Text("Pergunta 1: Qual o resultado de 2 + 2?"), ft.TextField(on_submit=calcular)]),
        ft.Column([ft.Text("Pergunta 2: Qual o resultado de 2 x 2?"), ft.TextField(on_submit=calcular)]),
        ft.Column([ft.Text("Pergunta 3: Qual o resultado de 8 / 4?"), ft.TextField(on_submit=calcular)]),
        ft.Column([ft.Text("Pergunta 4: Qual o resultado de 14 - 7?"), ft.TextField(on_submit=calcular)]),
        ft.Column([ft.Text("Pergunta 5: Qual o resultado de 2 ^ 3?"), ft.TextField(on_submit=calcular)]),
    ]
    
    # Adiciona a primeira pergunta ao layout
    av.view.add(perguntas[0])

# Inicia a aplicação
ft.app(target=main)
