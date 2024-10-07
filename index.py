import flet as ft

# Variáveis globais
etapa = 1
erros = 0
acertos = 0

# Respostas esperadas
resp_esp1 = ["7", "x=7"]
resp_esp2 = ["18", "y=18"]
resp_esp3 = ["3x+24=-x+4", "3x+24=4-x", "-x+4=3x+24"]
resp_esp4 = ["4x=-20", "-20=4x", "3x+x=4-24"]
resp_esp5 = ["x=-5"]
resp_esp6 = ["y=9"]

# Função para verificar respostas
def verificar_resposta(resposta, resp_esperada):
    global acertos, erros
    if resposta in resp_esperada:
        acertos += 1
        return True
    else:
        erros += 1
        return False

def main(page: ft.Page):
    global etapa
    
    def verificar():
        global etapa
        if etapa == 1:
            if verificar_resposta(resposta_5.value.strip().lower(), resp_esp1):
                page.add(ft.Text("Você acertou a primeira etapa!"))
                etapa += 1
                pergunta_6.visible = True
                resposta_6.visible = True
            else:
                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))
        
        elif etapa == 2:
            if verificar_resposta(resposta_6.value.strip().lower(), resp_esp2):
                page.add(ft.Text("Você acertou a segunda etapa!"))
                etapa += 1
                pergunta_7.visible = True
                resposta_7.visible = True
            else:
                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))
       
        elif etapa == 3:
            if verificar_resposta(resposta_6.value.strip().lower(), resp_esp2):
                page.add(ft.Text("Você acertou a segunda etapa!"))
                etapa += 1
                pergunta_7.visible = True
                resposta_7.visible = True
            else:
                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))

        elif etapa == 4:
            if verificar_resposta(resposta_6.value.strip().lower(), resp_esp2):
                page.add(ft.Text("Você acertou a segunda etapa!"))
                etapa += 1
                pergunta_7.visible = True
                resposta_7.visible = True
            else:
                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))

        elif etapa == 5:
            if verificar_resposta(resposta_6.value.strip().lower(), resp_esp2):
                page.add(ft.Text("Você acertou a segunda etapa!"))
                etapa += 1
                pergunta_7.visible = True
                resposta_7.visible = True
            else:
                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))

        # Continue para as próximas etapas

    # Interface
    page.title = "Tutor de Matemática"
    
    # Pergunta 1
    pergunta_5 = ft.Text("1) Encontre o valor de y fazendo a substituição necessária. Dada a reta y = 2x + 3, qual o valor de y quando x = 2?")
    resposta_5 = ft.TextField(label="Sua resposta")
    verificar_button_5 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar())
    
    # Pergunta 2
    pergunta_6 = ft.Text("2) Dada a reta y = 2x + 2, encontre o valor de x quando y = 8.", visible=False)
    resposta_6 = ft.TextField(label="Sua resposta", visible=False)
    verificar_button_6 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar(), visible=False)

    page.add(pergunta_5, resposta_5, verificar_button_5, pergunta_6, resposta_6, verificar_button_6)

ft.app(target=main)
