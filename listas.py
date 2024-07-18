linha1 = ["⬜️","️⬜️","️⬜️"]
linha2 = ["⬜️","⬜️","️⬜️"]
linha3 = ["⬜️️","⬜️️","⬜️️"]
mapa = [linha1, linha2, linha3]

print("Escondendo o tesouro! X marca o local.")
posicao = input("Onde você quer colocar o tesouro? Digite a posição (ex: a1, b2, c3): ")  # Onde você quer colocar o tesouro?
letra = posicao[0].lower()
abc = ['a', 'b', 'c']

indice_letra = abc.index(letra)
indice_numero = int(posicao[1]) - 1
mapa[indice_numero][indice_letra] = 'X'

print(f"{linha1}\n{linha2}\n{linha3}")
