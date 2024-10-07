{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "270aeb39",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import messagebox\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg\n",
    "# Função para centralizar a janela na tela\n",
    "def centralizar_janela(janela, largura, altura):\n",
    "    largura_tela = root.winfo_screenwidth()\n",
    "    altura_tela = root.winfo_screenheight()\n",
    "    pos_x = (largura_tela // 2) - (largura // 2)\n",
    "    pos_y = (altura_tela // 2) - (altura // 2)\n",
    "    janela.geometry(f\"{largura}x{altura}+{pos_x}+{pos_y}\")\n",
    "\n",
    "# Função para criar uma janela de aviso personalizada\n",
    "def mostrar_aviso(mensagem, dica=\"\"):\n",
    "    aviso_janela = tk.Toplevel(root)\n",
    "    aviso_janela.title(\"Atenção\")\n",
    "    \n",
    "    # Configurando a janela de aviso\n",
    "    largura = 400\n",
    "    altura = 200\n",
    "    centralizar_janela(aviso_janela, largura, altura)\n",
    "    aviso_janela.configure(bg=\"lightyellow\")\n",
    "\n",
    "    # Texto da mensagem com fonte maior\n",
    "    label_aviso = tk.Label(aviso_janela, text=mensagem, font=(\"Arial\", 16), bg=\"lightyellow\", fg=\"orange\", wraplength=350)\n",
    "    label_aviso.pack(pady=10)\n",
    "\n",
    "    # Texto da dica, se houver\n",
    "    if dica:\n",
    "        label_dica = tk.Label(aviso_janela, text=dica, font=(\"Arial\", 14), bg=\"lightyellow\", wraplength=350)\n",
    "        label_dica.pack(pady=10)\n",
    "\n",
    "    # Botão OK para fechar a janela\n",
    "    botao_ok = tk.Button(aviso_janela, text=\"OK\", command=aviso_janela.destroy, font=(\"Arial\", 14), bg=\"red\", fg=\"white\")\n",
    "    botao_ok.pack(pady=10)\n",
    "\n",
    "# Função para criar uma janela de sucesso personalizada\n",
    "def mostrar_sucesso(mensagem):\n",
    "    sucesso_janela = tk.Toplevel(root)\n",
    "    sucesso_janela.title(\"Sucesso\")\n",
    "\n",
    "    # Configurando a janela de sucesso\n",
    "    largura = 400\n",
    "    altura = 200\n",
    "    centralizar_janela(sucesso_janela, largura, altura)\n",
    "    sucesso_janela.configure(bg=\"lightgreen\")\n",
    "\n",
    "    # Texto da mensagem com fonte maior\n",
    "    label_sucesso = tk.Label(sucesso_janela, text=mensagem, font=(\"Arial\", 16), bg=\"lightgreen\", fg=\"green\", wraplength=350)\n",
    "    label_sucesso.pack(pady=20)\n",
    "\n",
    "    # Botão OK para fechar a janela\n",
    "    botao_ok = tk.Button(sucesso_janela, text=\"OK\", command=sucesso_janela.destroy, font=(\"Arial\", 14), bg=\"green\", fg=\"white\")\n",
    "    botao_ok.pack(pady=10)\n",
    "\n",
    "    \n",
    "    \n",
    "# Função para calcular e verificar as respostas\n",
    "def calcular():\n",
    "    global etapa, erros, acertos\n",
    "    if etapa == 1:\n",
    "        resposta_usuario = resposta_5.get().strip().lower()\n",
    "        if resposta_usuario in [resp.lower() for resp in resp_esp5]:\n",
    "            mostrar_sucesso(\"Você acertou a primeira etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Sua resposta não está correta, tente novamente.\", \n",
    "                          \"Dica: reescreva a equação substituindo o valor de x e efetue as operações.\")\n",
    "            erros += 1\n",
    "    elif etapa == 2:\n",
    "        resposta_usuario = resposta_6.get().strip().lower()\n",
    "        if resposta_usuario == \"8=2x+2\":\n",
    "            mostrar_sucesso(\"Você acertou a segunda etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Sua resposta não está correta, tente novamente.\", \n",
    "                          \"Dica: reescreva a equação substituindo o valor de y.\")\n",
    "            erros += 1\n",
    "    elif etapa == 3:\n",
    "        resposta_usuario = resposta_6b.get().strip().lower()\n",
    "        if resposta_usuario in [\"2x=6\", \"6=2x\"]:\n",
    "            mostrar_sucesso(\"Você acertou a terceira etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Sua resposta não está correta, tente novamente.\", \n",
    "                          \"Dica: subtraia 2 nos dois lados da equação.\")\n",
    "            erros += 1\n",
    "    elif etapa == 4:\n",
    "        resposta_usuario = resposta_6c.get().strip().lower()\n",
    "        if resposta_usuario in [\"x=3\", \"3\"]:\n",
    "            mostrar_sucesso(\"Você acertou a quarta etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mudar_pagina(3)  # Muda para a página das perguntas 1 a 4\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Sua resposta não está correta, tente novamente.\", \n",
    "                          \"Dica: divida por 2 nos dois lados da equação.\")\n",
    "            erros += 1\n",
    "    elif etapa == 5:\n",
    "        resposta_usuario = resposta_1.get().strip().lower()\n",
    "        if resposta_usuario in [resp.lower() for resp in resp_esp1]:\n",
    "            mostrar_sucesso(\"Você acertou a quinta etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Sua resposta não está correta, tente novamente.\", \n",
    "                          \"Dica: iguale as equações das retas f e g.\")\n",
    "            erros += 1\n",
    "    elif etapa == 6:\n",
    "        resposta_usuario = resposta_2.get().strip().lower()\n",
    "        if resposta_usuario in [resp.lower() for resp in resp_esp2]:\n",
    "            mostrar_sucesso(\"Você acertou a sexta etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Sua resposta não está correta, tente novamente.\", \n",
    "                          \"Dica: Isole o X em um dos lados da equação.\")\n",
    "            erros += 1\n",
    "    \n",
    "    elif etapa == 7:\n",
    "        resposta_usuario = resposta_3.get().strip().lower()\n",
    "        if resposta_usuario in [resp.lower() for resp in resp_esp3]:\n",
    "            mostrar_sucesso(\"Você acertou a sétima etapa!\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            mostrar_proxima_pergunta()\n",
    "        else:\n",
    "            mostrar_aviso(\"Atenção\", \"Sua resposta não está correta, tente novamente. \\nDica: Divida ambos os membros da equação por 4.\")\n",
    "            erros += 1    \n",
    "           \n",
    "    elif etapa == 8:\n",
    "        resposta_usuario = resposta_4.get().strip().lower()\n",
    "        if resposta_usuario in [resp.lower() for resp in resp_esp4]:\n",
    "            mostrar_sucesso(\"Sucesso: Você acertou todas as etapas! \\n \\nO ponto de interseção das retas f e g é  x = -5 e y = 9\")\n",
    "            acertos += 1\n",
    "            etapa += 1\n",
    "            root.after(100, lambda: mudar_pagina(8))\n",
    "            \n",
    "        else:\n",
    "            mostrar_aviso(\"Atenção\", \"Sua resposta não está correta, tente novamente. \\nDica: substitua o valor de X em alguma das equações f ou g.\")\n",
    "            erros += 1    \n",
    "\n",
    "# Função para mostrar as perguntas subsequentes na mesma página\n",
    "def mostrar_proxima_pergunta():\n",
    "    global etapa\n",
    "    if etapa == 2:\n",
    "        pergunta_6.pack(pady=20)\n",
    "        resposta_6.pack()\n",
    "        verificar_button_6.pack(pady=3)\n",
    "    elif etapa == 3:\n",
    "        pergunta_6b.pack(pady=20)\n",
    "        resposta_6b.pack()\n",
    "        verificar_button_6b.pack(pady=3)\n",
    "    elif etapa == 4:\n",
    "        pergunta_6c.pack(pady=20)\n",
    "        resposta_6c.pack()\n",
    "        verificar_button_6c.pack(pady=3)\n",
    "    elif etapa == 5:\n",
    "        pergunta_1.pack(pady=20)\n",
    "        resposta_1.pack()\n",
    "        verificar_button_1.pack(pady=3)\n",
    "    elif etapa == 6:\n",
    "        pergunta_2.pack(pady=20)\n",
    "        resposta_2.pack()\n",
    "        verificar_button_2.pack(pady=3)      \n",
    "    elif etapa == 7:\n",
    "        pergunta_3.pack(pady=20)\n",
    "        resposta_3.pack()\n",
    "        verificar_button_3.pack(pady=3)\n",
    "    elif etapa == 8:\n",
    "        pergunta_4.pack(pady=20)\n",
    "        resposta_4.pack()\n",
    "        verificar_button_4.pack(pady=3)\n",
    "\n",
    "# Função para mudar de página\n",
    "def mudar_pagina(pagina):\n",
    "    frame_welcome.pack_forget()\n",
    "    frame_1.pack_forget()\n",
    "    frame_2.pack_forget()\n",
    "    frame_results.pack_forget()\n",
    "\n",
    "    if pagina == 1:\n",
    "        frame_welcome.pack(fill=\"both\", expand=1)\n",
    "    elif pagina == 2:\n",
    "        frame_1.pack(fill=\"both\", expand=1)\n",
    "    elif pagina == 3:\n",
    "        frame_2.pack(fill=\"both\", expand=1)\n",
    "    elif pagina == 8:\n",
    "        frame_results.pack(fill=\"both\", expand=1)\n",
    "        mostrar_grafico()  # Adiciona o gráfico à página de resultados\n",
    "\n",
    "# Função para mostrar resultados gráficos\n",
    "def mostrar_grafico():\n",
    "    global acertos, erros\n",
    "\n",
    "    # Dados para o gráfico\n",
    "    categorias = ['Corretas', 'Erradas']\n",
    "    valores = [acertos, erros]\n",
    "\n",
    "    # Criação do gráfico\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.bar(categorias, valores, color=['green', 'red'])\n",
    "    ax.set_xlabel('Resultado')\n",
    "    ax.set_ylabel('Número de Perguntas')\n",
    "    ax.set_title('Resultados do Quiz')\n",
    "\n",
    "    # Adiciona o gráfico ao frame de resultados\n",
    "    canvas = FigureCanvasTkAgg(fig, master=frame_results)\n",
    "    canvas.draw()\n",
    "    canvas.get_tk_widget().pack()\n",
    "\n",
    "# Configuração inicial\n",
    "etapa = 1\n",
    "erros = 0\n",
    "acertos = 0\n",
    "resp_esp1 = [\"3x+24=-x+4\", \"3x+24=4-x\", \"-x+4=3x+24\", \"-x+4=24+3x\", \"4-x=24+3x\", \"4-x=3x+24\", \"24+3x=-x+4\", \"24+3x=4-x\"]\n",
    "resp_esp2 = [\"4x=-20\", \"-20=4x\", \"3x+x=4-24\", \"24-4=-x-3x\"]\n",
    "resp_esp3 = [\"x=-5\", \"x = -5\", \"-5\"]\n",
    "resp_esp4 = [\"y=9\", \"y = 9\", \"9\"] \n",
    "resp_esp5 = [\"y=7\", \"7\", \"y = 7\", \"y=2*2+3\", \"y = 2*2 + 3\", \"y=4+3\", \"y = 4 + 3\"]\n",
    "resp_esp6 = [\"8=2x+2\", \"2x=6\", \"6=2x\", \"2x = 6\", \"6 = 2x\"]\n",
    "\n",
    "# Criar a janela principal\n",
    "root = tk.Tk()\n",
    "root.title(\"Tutor de Matemática\")\n",
    "root.configure(bg=\"lightgreen\")\n",
    "\n",
    "# Página de Boas-vindas\n",
    "frame_welcome = tk.Frame(root)\n",
    "welcome_label = tk.Label(frame_welcome, text=\"Bem-vindo ao Tutor de Matemática!\", font=(\"Arial\", 20))\n",
    "welcome_label.pack(pady=20)\n",
    "\n",
    "instructions_label = tk.Label(\n",
    "    frame_welcome, \n",
    "    text=\"Este tutorial irá guiá-lo através de várias etapas para resolver equações e sistemas de equações. \\n \\nPara cada pergunta, insira a resposta na caixa fornecida e clique em 'Verificar'. \\n \\nSe você errar, receberá uma dica para tentar novamente. \\n \\nVamos começar!\", \n",
    "    font=(\"Arial\", 16)  \n",
    ")\n",
    "instructions_label.pack(pady=20)\n",
    "\n",
    "start_button = tk.Button(frame_welcome, text=\"Começar\", command=lambda: mudar_pagina(2), bg=\"blue\", fg=\"white\")\n",
    "start_button.pack(pady=20)\n",
    "\n",
    "# Página das Perguntas 1 a 4\n",
    "frame_1 = tk.Frame(root, bg=\"lightgreen\")\n",
    "frame_1.pack(fill=\"both\", expand=1)\n",
    "\n",
    "pergunta_5 = tk.Label(frame_1, text=\"1) Encontre o valor de y fazendo a substituição necessária. \\n \\nDada a reta y = 2x + 3, qual o valor de y quando x = 2\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "pergunta_5.pack(pady=20)\n",
    "resposta_5 = tk.Entry(frame_1, font=(\"Arial\", 14))\n",
    "resposta_5.pack()\n",
    "\n",
    "pergunta_6 = tk.Label(frame_1, text=\"2) Dada a reta y = 2x + 2, encontre o valor de x quando y = 8. \\n \\nATENÇÃO: Nas próximas etapas insira apenas a substituição necessária.\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_6 = tk.Entry(frame_1, font=(\"Arial\", 14))\n",
    "\n",
    "pergunta_6b = tk.Label(frame_1, text=\"3) Nossa equação agora é 8 = 2x + 2\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_6b = tk.Entry(frame_1, font=(\"Arial\", 14))\n",
    "\n",
    "pergunta_6c = tk.Label(frame_1, text=\"4) Resolva x em 2x=6? \\nInsira o valor final de x\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_6c = tk.Entry(frame_1, font=(\"Arial\", 14))\n",
    "\n",
    "verificar_button_5 = tk.Button(frame_1, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "verificar_button_5.pack(pady=3)\n",
    "verificar_button_6 = tk.Button(frame_1, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "verificar_button_6b = tk.Button(frame_1, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "verificar_button_6c = tk.Button(frame_1, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "\n",
    "# Página das Perguntas 7 a 8\n",
    "frame_2 = tk.Frame(root, bg=\"lightgreen\")\n",
    "frame_2.pack(fill=\"both\", expand=1)\n",
    "\n",
    "pergunta_1 = tk.Label(frame_2, text=\"5) Duas retas f e g se encontram e determinam um ponto de interseção. \\nO Ponto de interseção é o lugar no plano cartesiano onde duas retas se encontram, \\nEsse ponto é caracterizado por ter coordenadas (x , y) que satisfazem ao mesmo tempo as equações de duas retas. \\n \\nEncontre o ponto de interseção das retas f e g, sendo, f: y = 3x + 24 e g: y= -x + 4\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_1 = tk.Entry(frame_2, font=(\"Arial\", 14))\n",
    "\n",
    "pergunta_2 = tk.Label(frame_2, text=\"6) Nossa equação agora é 3x + 24 = -x + 4.\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_2 = tk.Entry(frame_2, font=(\"Arial\", 14))\n",
    "\n",
    "pergunta_3 = tk.Label(frame_2, text=\"7) Isolando x, temos a equação: 4x = -20, resolva para encontrar o valor de x. \\nInsira o valor final de x.\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_3 = tk.Entry(frame_2, font=(\"Arial\", 14))\n",
    "\n",
    "pergunta_4 = tk.Label(frame_2, text=\"Agora, sabendo que x = -5 encontre o valor y. \\nInsira o valor final de y.\", bg=\"lightgreen\", font=(\"Arial\", 14))\n",
    "resposta_4 = tk.Entry(frame_2, font=(\"Arial\", 14))\n",
    "\n",
    "verificar_button_1 = tk.Button(frame_2, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "verificar_button_2 = tk.Button(frame_2, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "verificar_button_3 = tk.Button(frame_2, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "verificar_button_4 = tk.Button(frame_2, text=\"Verificar\", command=calcular, bg=\"blue\", fg=\"white\")\n",
    "\n",
    "# Página de Resultados\n",
    "frame_results = tk.Frame(root)\n",
    "resultados_button = tk.Button(frame_results, text=\"Mostrar Resultados\", command=mostrar_grafico, bg=\"blue\", fg=\"white\")\n",
    "resultados_button.pack(pady=20)\n",
    "\n",
    "# Exibir a página de boas-vindas ao iniciar\n",
    "mudar_pagina(1)\n",
    "\n",
    "# Iniciar o loop da interface gráfica\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fec1c035",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8db5402d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
