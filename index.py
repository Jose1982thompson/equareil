import flet as ft
import matplotlib.pyplot as plt
import io
from base64 import b64encode

# Função para gerar gráfico como uma imagem base64
def gerar_grafico(acertos, erros):
    categorias = ['Corretas', 'Erradas']
    valores = [acertos, erros]

    fig, ax = plt.subplots()
    ax.bar(categorias, valores, color=['green', 'red'])
    ax.set_xlabel('Resultado')
    ax.set_ylabel('Número de Perguntas')
    ax.set_title('Resultados do Quiz')

    # Converter o gráfico em base64 para exibir no Flet
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = b64encode(buf.read()).decode('utf-8')
    buf.close()
    return f"data:image/png;base64,{img_base64}"

# Função para verificar as respostas e avançar
def verificar_resposta(page, etapa, acertos, erros, respostas, resposta_usuario, dica):
    if resposta_usuario in respostas:
        acertos += 1
        page.controls.append(ft.Text("Você acertou!", color="green"))
    else:
        erros += 1
        page.controls.append(ft.Text(f"Sua resposta está errada. Dica: {dica}", color="red"))
    return acertos, erros

# Função principal do aplicativo Flet
def main(page: ft.Page):
    page.title = "Tutor de Matemática"
    page.bgcolor = ft.colors.LIGHT_GREEN

    etapa = 1
    acertos = 0
    erros = 0

    def avancar_etapa(e):
        nonlocal etapa, acertos, erros

        if etapa == 1:
            resposta_usuario = resposta_1.value.strip().lower()
            acertos, erros = verificar_resposta(page, etapa, acertos, erros, ["y=7", "7", "y = 7"], resposta_usuario, "Substitua o valor de x na equação.")
            etapa += 1
        elif etapa == 2:
            resposta_usuario = resposta_2.value.strip().lower()
            acertos, erros = verificar_resposta(page, etapa, acertos, erros, ["8=2x+2"], resposta_usuario, "Reescreva a equação com o valor de y.")
            etapa += 1
        elif etapa == 3:
            resposta_usuario = resposta_3.value.strip().lower()
            acertos, erros = verificar_resposta(page, etapa, acertos, erros, ["2x=6"], resposta_usuario, "Subtraia 2 nos dois lados da equação.")
            etapa += 1
        elif etapa == 4:
            resposta_usuario = resposta_4.value.strip().lower()
            acertos, erros = verificar_resposta(page, etapa, acertos, erros, ["x=3"], resposta_usuario, "Divida por 2 nos dois lados da equação.")
            etapa += 1

        # Atualizar o gráfico ao final
        if etapa > 4:
            img_data = gerar_grafico(acertos, erros)
            page.controls.append(ft.Image(src=img_data))

        page.update()

    # Layout de perguntas
    pergunta_1 = ft.Text("1) Qual o valor de y quando x = 2, dada a reta y = 2x + 3?")
    resposta_1 = ft.TextField(label="Resposta")
    
    pergunta_2 = ft.Text("2) Qual o valor de x quando y = 8, dada a reta y = 2x + 2?")
    resposta_2 = ft.TextField(label="Resposta")
    
    pergunta_3 = ft.Text("3) Nossa equação agora é 8 = 2x + 2. Resolva para x.")
    resposta_3 = ft.TextField(label="Resposta")
    
    pergunta_4 = ft.Text("4) Resolva x em 2x = 6?")
    resposta_4 = ft.TextField(label="Resposta")

    # Botão para avançar
    verificar_button = ft.ElevatedButton(text="Verificar", on_click=avancar_etapa)

    # Adicionar controles à página
    page.controls.append(pergunta_1)
    page.controls.append(resposta_1)
    page.controls.append(pergunta_2)
    page.controls.append(resposta_2)
    page.controls.append(pergunta_3)
    page.controls.append(resposta_3)
    page.controls.append(pergunta_4)
    page.controls.append(resposta_4)
    page.controls.append(verificar_button)

    page.update()

ft.app(target=main)
