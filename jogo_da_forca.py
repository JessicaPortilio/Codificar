import random

# Estágios do enforcado
estagios = [r'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
''', r'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
''', r'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
''', r'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
''', r'''
    +---+
    |   |
        |
        |
        |
        |
  =========
''']

# Logo do jogo
logo = r'''
J)jjjjjj  O)oooo    G)gggg  O)oooo     D)dddd     A)aa      F)ffffff  O)oooo  R)rrrrr    C)ccc    A)aa   
    J)   O)    oo  G)      O)    oo    D)   dd   A)  aa     F)       O)    oo R)    rr  C)   cc  A)  aa  
    J)   O)    oo G)  ggg  O)    oo    D)    dd A)    aa    F)fffff  O)    oo R)  rrr  C)       A)    aa 
J)  jj   O)    oo G)    gg O)    oo    D)    dd A)aaaaaa    F)       O)    oo R) rr    C)       A)aaaaaa 
J)  jj   O)    oo  G)   gg O)    oo    D)    dd A)    aa    F)       O)    oo R)   rr   C)   cc A)    aa 
 J)jj     O)oooo    G)ggg   O)oooo     D)ddddd  A)    aa    F)        O)oooo  R)    rr   C)ccc  A)    aa 
'''

# Lista de palavras para o jogo
lista_de_palavras = [
    'abacaxi', 'abacate', 'açaí', 'acerola', 'amora', 'banana', 'caju', 'caqui', 'carambola', 
    'cereja', 'coco', 'figo', 'framboesa', 'goiaba', 'graviola', 'jabuticaba', 'jaca', 'kiwi', 
    'laranja', 'limão', 'lichia', 'maçã', 'mamão', 'manga', 'maracujá', 'melancia', 'melão', 
    'morango', 'nectarina', 'pera', 'pêssego', 'pitanga', 'pitaya', 'romã', 'tangerina', 'uva'
]

print(logo)
# Escolher uma palavra aleatória da lista
palavra_escolhida = random.choice(lista_de_palavras)
tamanho_palavra = len(palavra_escolhida)

fim_do_jogo = False
vidas = 6

# Criar espaços em branco para a palavra
display = ["_" for _ in range(tamanho_palavra)]

while not fim_do_jogo:
    palpite = input("Adivinhe uma letra: ").lower()

    # Verificar se a letra já foi adivinhada
    if palpite in display:
        print(f"Você já adivinhou a letra {palpite}")
        continue

    # Verificar a letra adivinhada
    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == palpite:
            display[posicao] = letra

    # Verificar se o palpite está errado
    if palpite not in palavra_escolhida:
        print(f"Você digitou {palpite}, que não está na palavra. Você perde uma vida.")
        vidas -= 1
        if vidas == 0:
            fim_do_jogo = True
            print("Você perdeu.")

    # Exibir o estado atual da palavra
    print(f"{' '.join(display)}")
    print(estagios[vidas])

    # Verificar se o usuário ganhou
    if "_" not in display:
        fim_do_jogo = True
        print("Você ganhou.")