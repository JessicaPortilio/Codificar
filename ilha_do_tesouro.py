# Nesse link você consegue essas artes
# https://ascii.co.uk/art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")

# Escreva seu código abaixo desta linha 👇

escolha1 = input('Você está em uma encruzilhada. Para onde você quer ir? Digite "esquerda" ou "direita" \n').lower()
if escolha1 == "esquerda":
    escolha2 = input('Você chegou a um lago. Há uma ilha no meio do lago. Digite "esperar" para esperar por um barco. Digite "nadar" para nadar até lá. \n').lower()
    if escolha2 == "esperar":
        escolha3 = input("Você chega à ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? \n").lower()
        if escolha3 == "vermelha":
            print("É uma sala cheia de fogo. Fim de jogo.")
        elif escolha3 == "amarela":
            print("Você encontrou o tesouro! Você venceu!")
        elif escolha3 == "azul":
            print("Você entra em uma sala de bestas. Fim de jogo.")
        else:
            print("Você escolheu uma porta que não existe. Fim de jogo.")
    else:
        print("Você é atacado por uma truta furiosa. Fim de jogo.")
else:
    print("Você caiu em um buraco. Fim de jogo.")
