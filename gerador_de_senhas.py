import random

# Listas de letras, números e símbolos que serão usadas para gerar a senha
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Mensagem de boas-vindas ao gerador de senhas
print("Bem-vindo ao Gerador de Senhas PyPassword!")

# Solicitando ao usuário o número de letras que ele quer na senha
nr_letras = int(input("Quantas letras você gostaria na sua senha?\n")) 

# Solicitando ao usuário o número de símbolos que ele quer na senha
nr_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))

# Solicitando ao usuário o número de números que ele quer na senha
nr_numeros = int(input(f"Quantos números você gostaria?\n"))

# Nível Fácil 
# # Cria uma senha simples sem embaralhar
# senha = ""
# 
# # Adiciona as letras à senha
# for char in range(1, nr_letras + 1):
#   senha += random.choice(letras)
# 
# # Adiciona os símbolos à senha
# for char in range(1, nr_simbolos + 1):
#   senha += random.choice(simbolos)
# 
# # Adiciona os números à senha
# for char in range(1, nr_numeros + 1):
#   senha += random.choice(numeros)
# 
# # Imprime a senha gerada
# print(senha)

# Nível Difícil (Senha embaralhada)

# Cria uma lista para armazenar os caracteres da senha
lista_senha = []

# Adiciona letras aleatórias à lista de senha
for char in range(1, nr_letras + 1):
    lista_senha.append(random.choice(letras))

# Adiciona símbolos aleatórios à lista de senha
for char in range(1, nr_simbolos + 1):
    lista_senha += random.choice(simbolos)

# Adiciona números aleatórios à lista de senha
for char in range(1, nr_numeros + 1):
    lista_senha += random.choice(numeros)

# Imprime a lista de caracteres antes de embaralhar
print(lista_senha)

# Embaralha a lista de caracteres
random.shuffle(lista_senha)

# Imprime a lista de caracteres após embaralhar
print(lista_senha)

# Converte a lista de caracteres em uma string de senha
senha = ""
for char in lista_senha:
    senha += char

# Imprime a senha gerada
print(f"Sua senha é: {senha}")
