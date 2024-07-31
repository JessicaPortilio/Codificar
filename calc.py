import tkinter as tk
from tkinter import messagebox

# Função chamada quando um botão de número ou operação é clicado
def ao_clicar_botao(event):
    texto_atual = entrada.get()  # Pega o texto atual do campo de entrada
    novo_texto = texto_atual + event.widget.cget("text")  # Adiciona o texto do botão clicado ao texto atual
    entrada.delete(0, tk.END)  # Limpa o campo de entrada
    entrada.insert(0, novo_texto)  # Insere o novo texto no campo de entrada

# Função chamada quando o botão de limpar (C) é clicado
def ao_limpar(event):
    entrada.delete(0, tk.END)  # Limpa o campo de entrada

# Função chamada quando o botão de igual (=) é clicado
def ao_igual(event):
    try:
        resultado = eval(entrada.get())  # Avalia a expressão matemática no campo de entrada
        entrada.delete(0, tk.END)  # Limpa o campo de entrada
        # Verifica se o resultado é um número inteiro
        if isinstance(resultado, int) or resultado.is_integer():
            print(resultado)
            entrada.insert(0, str(int(resultado)))
        else:
            entrada.insert(0, str(resultado))  # Insere o resultado no campo de entrada
    except Exception as e:
        messagebox.showerror("Erro", "Entrada inválida")  # Mostra uma mensagem de erro se a expressão for inválida

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")  # Define o título da janela
root.geometry("320x450")  # Define o tamanho da janela
root.config(bg="#282828")  # Define a cor de fundo da janela

# Estilo
fonte_entrada = ("Arial", 24)  # Define a fonte para o campo de entrada
fonte_botao = ("Arial", 18, "bold")  # Define a fonte para os botões
botao_bg = "#b0abab"  # Define a cor de fundo dos botões
botao_fg = "black"  # Define a cor do texto dos botões
botao_active_bg = "#b0abab"  # Define a cor de fundo dos botões quando clicados

# Campo de entrada
entrada = tk.Entry(root, font=fonte_entrada, bd=10, insertwidth=4, width=14, borderwidth=4, bg="#FFFFFF")
# Cria um campo de entrada onde o usuário verá os números e operações digitados
entrada.grid(row=0, column=0, columnspan=4, pady=20)  # Posiciona o campo de entrada na janela

# Lista de botões da calculadora
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Posicionamento dos botões
linha = 1
coluna = 0

# Cria e posiciona cada botão na janela
for botao in botoes:
    acao = lambda x=botao: ao_clicar_botao(x)  # Define a ação para quando o botão é clicado
    b = tk.Button(root, text=botao, font=fonte_botao, bg=botao_bg, fg=botao_fg, activebackground=botao_active_bg, height=2, width=4)
    # Cria um botão com as configurações de estilo definidas
    b.bind("<Button-1>", acao)  # Liga a ação de clicar ao botão
    b.grid(row=linha, column=coluna, padx=5, pady=5)  # Posiciona o botão na janela

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Ligações especiais para os botões de limpar (C) e igual (=)
botao_limpar = root.grid_slaves(row=4, column=0)[0]
botao_limpar.bind("<Button-1>", ao_limpar)

botao_igual = root.grid_slaves(row=4, column=2)[0]
botao_igual.bind("<Button-1>", ao_igual)

# Inicia a aplicação
root.mainloop()
