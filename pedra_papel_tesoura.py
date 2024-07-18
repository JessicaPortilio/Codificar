import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagens_jogo = [pedra, papel, tesoura]

while True:
    # Solicita a escolha do usuário
    escolha_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))

    # Verifica se a escolha do usuário é válida
    if escolha_usuario >= 3 or escolha_usuario < 0: 
        print("Você digitou um número inválido, você perde!") 
    else:
        # Exibe a escolha do usuário
        print(imagens_jogo[escolha_usuario])

        # Escolha do computador
        escolha_computador = random.randint(0, 2)
        print("O computador escolheu:")
        print(imagens_jogo[escolha_computador])

        # Determina o resultado do jogo
        if escolha_usuario == 0 and escolha_computador == 2:
            print("Você ganha!")
        elif escolha_computador == 0 and escolha_usuario == 2:
            print("Você perde")
        elif escolha_computador > escolha_usuario:
            print("Você perde")
        elif escolha_usuario > escolha_computador:
            print("Você ganha!")
        elif escolha_computador == escolha_usuario:
            print("É um empate")
        
        sair = input('Deseja continuar: S ou N: ')
        
        if sair == 'N' or sair == 'n':
            break