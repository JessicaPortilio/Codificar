from tkinter import * # Importa todas as funcionalidades do módulo tkinter
from tkinter import messagebox, ttk # Importa as funcionalidades específicas messagebox e ttk do tkinter
import secrets # Importa o módulo secrets, usado para gerar números e tokens aleatórios seguros
import string # Importa o módulo string, que contém várias constantes e funções úteis para manipulação de texto

# Função para gerar a senha segura
def gerar_senha():
    try:
        # Tenta obter o valor do comprimento da senha inserido pelo usuário
        tamanho = int(comprimento_senha_entry.get())
    except ValueError:
        # Se o valor não for um número válido, exibe uma mensagem de erro
        messagebox.showerror('Erro', 'Por favor, insira um número válido para o comprimento da senha!')
        return
    
    # Obtém os valores das variáveis booleanas associadas aos checkbuttons
    incluir_letras = var_letras.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()
    
    # Inicializa a string de caracteres vazia
    caracteres = ''
    if incluir_letras:
        # Adiciona letras à string de caracteres se o checkbutton de letras estiver marcado
        caracteres += string.ascii_letters
    if incluir_numeros:
        # Adiciona números à string de caracteres se o checkbutton de números estiver marcado
        caracteres += string.digits
    if incluir_simbolos:
        # Adiciona símbolos à string de caracteres se o checkbutton de símbolos estiver marcado
        caracteres += string.punctuation

    if not caracteres:
        # Se nenhum checkbutton estiver marcado, exibe uma mensagem de erro
        messagebox.showerror('Erro', 'Selecione pelo menos uma opção de caracteres!')
        return
    
    # Gera a senha usando caracteres aleatórios da string de caracteres
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    # Limpa o campo de entrada de senha e insere a nova senha gerada
    senha_entry.delete(0, END)
    senha_entry.insert(0, senha)
    
# Cria a janela principal da aplicação
janela = Tk()
janela.title('Gerador de Senhas Seguras') # Define o título da janela
janela.geometry('330x300') # Define o tamanho da janela
janela.config(bg="#f0f8ff") # Define a cor de fundo da janela

# Adiciona um título à janela
titulo = Label(janela, text='Gerador de Senhas Seguras', font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4682b4")
titulo.pack(padx=10, pady=10, side=TOP)

# Cria um frame para agrupar os widgets de entrada de comprimento da senha
frame_label = Frame(janela, bg="#f0f8ff")
frame_label.pack(padx=10, pady=10)

# Adiciona um label e um campo de entrada para o comprimento da senha
comprimento_senha_label = Label(frame_label, text='Comprimento da Senha:', bg="#f0f8ff", font=('Arial', 10, 'bold'))
comprimento_senha_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
comprimento_senha_entry = Entry(frame_label)
comprimento_senha_entry.grid(row=0, column=1, padx=5, pady=5,)

# Cria um frame para agrupar os checkbuttons
frame_check = Frame(janela, bg="#f0f8ff")
frame_check.pack()

# Adiciona um checkbutton para incluir letras na senha
var_letras = BooleanVar(value=True)
check_letras = Checkbutton(frame_check, text='Incluir Letras', variable= var_letras, bg="#f0f8ff",
                        activebackground="#f0f8ff")
check_letras.grid(row=1, column=0, sticky='w')

# Adiciona um checkbutton para incluir números na senha
var_numeros = BooleanVar(value=True)
check_numeros = Checkbutton(frame_check, text='Incluir Números', variable= var_numeros, bg="#f0f8ff",
                        activebackground="#f0f8ff")
check_numeros.grid(row=1, column=1, sticky='w')

# Adiciona um checkbutton para incluir símbolos na senha
var_simbolos = BooleanVar(value=True)
check_simbolos = Checkbutton(frame_check, text='Incluir Símbolos', variable= var_simbolos, bg="#f0f8ff",
                        activebackground="#f0f8ff")
check_simbolos.grid(row=1, column=2, sticky='w')

# Cria um frame para agrupar o botão de geração de senha e o campo de exibição da senha
frame_botao = Frame(janela, bg="#f0f8ff")
frame_botao.pack()

# Adiciona o botão que chama a função de geração de senha
botao_gerar = Button(frame_botao, text='Gerar Senha', bg="#4682b4", 
                    fg="white", font=("Helvetica", 10, "bold"), command=gerar_senha)
botao_gerar.grid(row=2, column=0, pady=20)

# Adiciona um campo de entrada onde a senha gerada será exibida
senha_entry = Entry(frame_botao, width=40)
senha_entry.grid(row=3, column=0, padx=10, pady=40)

# Inicia o loop principal da aplicação
janela.mainloop()
