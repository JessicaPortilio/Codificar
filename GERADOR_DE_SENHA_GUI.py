import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Função para gerar a senha segura
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para o comprimento da senha!")
        return

    incluir_letras = var_letras.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()

    caracteres = ''
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        messagebox.showerror("Erro", "Selecione pelo menos uma opção de caracteres!")
        return

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("330x300")
janela.configure(bg="#f0f8ff")

# Configuração do layout
titulo = tk.Label(janela, text="Gerador de Senhas Seguras", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4682b4")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(janela, text="Comprimento da Senha:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_tamanho = tk.Entry(janela)
entry_tamanho.grid(row=1, column=1, padx=10, pady=10)

var_letras = tk.BooleanVar(value=True)
check_letras = tk.Checkbutton(janela, text="Incluir Letras", var=var_letras, bg="#f0f8ff", activebackground="#f0f8ff")
check_letras.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

var_numeros = tk.BooleanVar(value=True)
check_numeros = tk.Checkbutton(janela, text="Incluir Números", var=var_numeros, bg="#f0f8ff", activebackground="#f0f8ff")
check_numeros.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')

var_simbolos = tk.BooleanVar(value=True)
check_simbolos = tk.Checkbutton(janela, text="Incluir Símbolos", var=var_simbolos, bg="#f0f8ff", activebackground="#f0f8ff")
check_simbolos.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='w')

botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha, bg="#4682b4", fg="white", font=("Helvetica", 10, "bold"))
botao_gerar.grid(row=5, column=0, columnspan=2, pady=10)

entry_senha = tk.Entry(janela, width=40)
entry_senha.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Inicia a janela
janela.mainloop()
