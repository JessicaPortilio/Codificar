from replit import clear

lances = {}

clear()
def encontre_o_maior_lance(lances):
    # Determina o nome e o valor do maior lance
    maior_lance = 0
    nome_maior_lance = ""
    for nome, valor in lances.items():
        if valor > maior_lance:
            maior_lance = valor
            nome_maior_lance = nome
    return maior_lance, nome_maior_lance
while True:

    nome = input('Informe seu nome: ')
    try:
        preco = float(input('Informe seu lance: R$ '))
        if preco <= 0:
                print("O lance deve ser um valor positivo. Tente novamente.")
    except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
            
    lances[nome] = preco

    outro_jogado = input('Tem mais jogadores para jogar [S]im ou [N]ão? ').lower()
    
    clear()
    if outro_jogado == 'n':
        break
    
maior_lance, nome_maior_lance = encontre_o_maior_lance(lances)


print(lances)
print(f'O maior lance foi de {nome_maior_lance} com R${maior_lance:.2f}')