import flet as ft
import re
import matplotlib.pyplot as plt
from io import BytesIO

# Função para validação de CPF ou outra lógica de cálculo
def validar_resposta(resposta_usuario, etapa):
    # Lógica para validar as respostas, com base nas etapas
    resp_esp5 = ["y=7", "7", "y=2*2+3", "y = 2*2 + 3", "y=4+3", "y = 4 + 3"]
    if etapa == 1 and resposta_usuario in [resp.lower() for resp in resp_esp5]:
        return True
    # Adicione outras verificações de etapas aqui...
    return False

# Função para exibir gráficos
def mostrar_grafico(acertos, erros, page):
    fig, ax = plt.subplots()
    categorias = ['Corretas', 'Erradas']
    valores = [acertos, erros]
    ax.bar(categorias, valores, color=['green', 'red'])
    ax.set_xlabel('Resultado')
    ax.set_ylabel('Número de Perguntas')
    ax.set_title('Resultados do Quiz')
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    image = ft.Image(src_base64=buf.read(), width=400, height=300)
    page.controls.append(image)
    page.update()

# Função principal para criar a interface com Flet
def main(page: ft.Page):
    page.title = "Tutor de Matemática"
    
    etapa = 1
    acertos = 0
    erros = 0

    resultado_texto = ft.Text()
    pergunta = ft.Text("1) Encontre o valor de y, dado que y = 2x + 3 quando x = 2:")
    resposta_input = ft.TextField(label="Sua resposta", width=250)

    def verificar_click(e):
        nonlocal etapa, acertos, erros
        resposta_usuario = resposta_input.value.strip().lower()
        if validar_resposta(resposta_usuario, etapa):
            resultado_texto.value = "Você acertou!"
            resultado_texto.color = ft.colors.GREEN
            acertos += 1
            etapa += 1
        else:
            resultado_texto.value = "Resposta incorreta. Tente novamente."
            resultado_texto.color = ft.colors.RED
            erros += 1

        # Exibir a próxima pergunta
        if etapa == 2:
            pergunta.value = "2) Dada a reta y = 2x + 2, encontre o valor de x quando y = 8."
        elif etapa == 3:
            pergunta.value = "3) Resolva a equação 2x=6."
        elif etapa > 3:
            resultado_texto.value = "Você concluiu todas as etapas!"
            mostrar_grafico(acertos, erros, page)
        
        page.update()

    # Botão para verificar a resposta
    verificar_button = ft.ElevatedButton(text="Verificar", on_click=verificar_click)

    # Adicionar elementos à página
    page.add(
        ft.Text("Bem-vindo ao Tutor de Matemática", style="headlineMedium"),
        pergunta,
        resposta_input,
        verificar_button,
        resultado_texto,
    )

# Executar a interface Flet
if __name__ == "__main__":
    ft.app(target=main)
