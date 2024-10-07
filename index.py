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

def calcular(resposta_usuario, resposta_correta, mensagem_sucesso, dica):
    global acertos, erros, etapa
    if resposta_usuario in resposta_correta:
        acertos += 1
        etapa += 1
        return f"{mensagem_sucesso}\nAcertos: {acertos}, Erros: {erros}"
    else:
        erros += 1
        return f"Sua resposta não está correta. Dica: {dica}\nAcertos: {acertos}, Erros: {erros}"

def on_start_click(e):
    welcome_page.visible = False
    question_page.visible = True
    page.update()

def verificar_etapa_1(e):
    resposta_usuario = resposta_5.value.strip().lower()
    resposta_correta = [resp.lower() for resp in resp_esp5]
    feedback = calcular(resposta_usuario, resposta_correta, "Você acertou a primeira etapa!", 
                        "Reescreva a equação substituindo o valor de x e efetue as operações.")
    resultado_label.value = feedback
    page.update()

# Configuração da página de boas-vindas
welcome_page = ft.Column([
    ft.Text("Bem-vindo ao Tutor de Matemática!", size=20),
    ft.Text("Este tutorial irá guiá-lo através de várias etapas para resolver equações."),
    ft.ElevatedButton("Começar", on_click=on_start_click),
])

# Configuração da página de perguntas
resposta_5 = ft.TextField(label="Resposta 1", width=300)
resultado_label = ft.Text()

question_page = ft.Column([
    ft.Text("1) Encontre o valor de y fazendo a substituição necessária. "
            "Dada a reta y = 2x + 3, qual o valor de y quando x = 2"),
    resposta_5,
    ft.ElevatedButton("Verificar", on_click=verificar_etapa_1),
    resultado_label,
])

# Configuração inicial da página
page = ft.Page(
    title="Tutor de Matemática",
    content=ft.Column([
        welcome_page,
        question_page,
    ])
)

# Iniciar o app
welcome_page.visible = True
question_page.visible = False

page.run()

