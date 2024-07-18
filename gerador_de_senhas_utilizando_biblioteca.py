import secrets
import string

def gerar_senha(tamanho=12):
    # Define o conjunto de caracteres que serão usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha de forma segura usando secrets.choice
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicita o tamanho da senha ao usuário
tamanho_senha = int(input("Qual o tamanho da senha que você deseja?\n"))

# Gera e imprime a senha
senha_gerada = gerar_senha(tamanho=tamanho_senha)
print(f"Sua senha é: {senha_gerada}")
