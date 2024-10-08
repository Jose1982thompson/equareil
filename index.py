import flet as ft



# Variáveis globais

etapa = 1

erros = 0

acertos = 0



# Respostas esperadas

resp_esp1 = ["7", "y=7"]

resp_esp2 = ["3", "x=3"]

resp_esp3 = ["3x+24=-x+4", "3x+24=4-x", "-x+4=3x+24"]

resp_esp4 = ["4x=-20", "-20=4x", "3x+x=4-24"]

resp_esp5 = ["x=-5", "-5"]

resp_esp6 = ["y=9", "9"]



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

            if verificar_resposta(resposta_1.value.strip().lower(), resp_esp1):

                page.add(ft.Text("Você acertou a primeira etapa!"))

                etapa += 1

                pergunta_1.visible = False

                resposta_1.visible = False

                verificar_button_1.visible = False

                pergunta_2.visible = True

                resposta_2.visible = True

                verificar_button_2.visible = True

                page.update()  # Atualiza a página imediatamente

            else:

                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))



        elif etapa == 2:

            if verificar_resposta(resposta_2.value.strip().lower(), resp_esp2):

                page.add(ft.Text("Você acertou a segunda etapa!"))

                etapa += 1

                pergunta_2.visible = False

                resposta_2.visible = False

                verificar_button_2.visible = False

                pergunta_3.visible = True

                resposta_3.visible = True

                verificar_button_3.visible = True

                page.update()

            else:

                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))



        elif etapa == 3:

            if verificar_resposta(resposta_3.value.strip().lower(), resp_esp3):

                page.add(ft.Text("Você acertou a terceira etapa!"))

                etapa += 1

                pergunta_3.visible = False

                resposta_3.visible = False

                verificar_button_3.visible = False

                pergunta_4.visible = True

                resposta_4.visible = True

                verificar_button_4.visible = True

                page.update()

            else:

                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))



        elif etapa == 4:

            if verificar_resposta(resposta_4.value.strip().lower(), resp_esp4):

                page.add(ft.Text("Você acertou a quarta etapa!"))

                etapa += 1

                pergunta_4.visible = False

                resposta_4.visible = False

                verificar_button_4.visible = False

                pergunta_5.visible = True

                resposta_5.visible = True

                verificar_button_5.visible = True

                page.update()

            else:

                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))



        elif etapa == 5:

            if verificar_resposta(resposta_5.value.strip().lower(), resp_esp5):

                page.add(ft.Text("Você acertou a quinta etapa!"))

                etapa += 1

                pergunta_5.visible = False

                resposta_5.visible = False

                verificar_button_5.visible = False

                pergunta_6.visible = True

                resposta_6.visible = True

                verificar_button_6.visible = True

                page.update()

            else:

                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))



        elif etapa == 6:

            if verificar_resposta(resposta_6.value.strip().lower(), resp_esp6):

                page.add(ft.Text("Você acertou a sexta etapa! Parabéns, você concluiu o exercício."))

                page.update()

                # Aqui você pode adicionar a lógica para exibir o gráfico de erros e acertos

            else:

                page.add(ft.Text("Sua resposta não está correta. Tente novamente."))



    # Interface

    page.title = "Tutor de Matemática"



    # Pergunta 1

    pergunta_1 = ft.Text("1) Encontre o valor de y fazendo a substituição necessária. Dada a reta y = 2x + 3, qual o valor de y quando x = 2?")

    resposta_1 = ft.TextField(label="Sua resposta")

    verificar_button_1 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar())



    # Pergunta 2

    pergunta_2 = ft.Text("2) Dada a reta y = 2x + 2, encontre o valor de x quando y = 8.", visible=False)

    resposta_2 = ft.TextField(label="Sua resposta", visible=False)

    verificar_button_2 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar(), visible=False)



    # Pergunta 3

    pergunta_3 = ft.Text("3) Duas retas f e g se encontram e determinam um ponto de interseção. O ponto de interseção é o lugar no plano cartesiano onde duas retas se encontram. Esse ponto é caracterizado por ter coordenadas (x, y) que satisfazem ao mesmo tempo as equações de duas retas. Encontre o ponto de interseção das retas f e g, sendo f: y = 3x + 24 e g: y = -x + 4. ATENÇÃO: Apenas reescreva a equação resolvendo passo a passo.", visible=False)

    resposta_3 = ft.TextField(label="Sua resposta", visible=False)

    verificar_button_3 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar(), visible=False)



    # Pergunta 4

    pergunta_4 = ft.Text("4) Nossa equação agora é 3x + 24 = -x + 4.", visible=False)

    resposta_4 = ft.TextField(label="Sua resposta", visible=False)

    verificar_button_4 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar(), visible=False)



    # Pergunta 5

    pergunta_5 = ft.Text("5) Isolando x, temos a equação: 4x = -20. Resolva para encontrar o valor de x. Insira o valor final de x.", visible=False)

    resposta_5 = ft.TextField(label="Sua resposta", visible=False)

    verificar_button_5 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar(), visible=False)



    # Pergunta 6

    pergunta_6 = ft.Text("6) Agora, sabendo que x = -5, encontre o valor de y. Insira o valor final de y.", visible=False)

    resposta_6 = ft.TextField(label="Sua resposta", visible=False)

    verificar_button_6 = ft.ElevatedButton("Verificar", on_click=lambda _: verificar(), visible=False)



    # Adiciona os componentes na página

    page.add(pergunta_1, resposta_1, verificar_button_1, pergunta_2, resposta_2, verificar_button_2,

             pergunta_3, resposta_3, verificar_button_3, pergunta_4, resposta_4, verificar_button_4,

             pergunta_5, resposta_5, verificar_button_5, pergunta_6, resposta_6, verificar_button_6)



ft.app(target=main)
