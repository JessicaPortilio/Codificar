alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

def codificar_decodificar(texto, deslocamento, operacao):
    texto_resultado = ''
    for i in texto:
        if i in alfabeto:  # Verifica se o caractere é uma letra
            indice = alfabeto.index(i)  # Obtém o índice da letra
            if operacao == 'decodificar':
                novo_indice = (indice - deslocamento) % len(alfabeto)  # Deslocamento para trás para descriptografar
            else:
                novo_indice = (indice + deslocamento) % len(alfabeto)  # Deslocamento para frente para criptografar
            
            letra_resultado = alfabeto[novo_indice]
            texto_resultado += letra_resultado
        else:
            texto_resultado += i  # Adiciona caracteres não alfabéticos sem alteração
    
    return texto_resultado

while True:
    opcao = input("Digite 'codificar' para criptografar, digite 'decodificar' para descriptografar (ou 'sair' para terminar):\n").lower()
    if opcao == 'sair':
        print("Saindo...")
        break

    texto = input('Digite sua mensagem:\n').lower()
    deslocamento = int(input('Digite o número do deslocamento:\n'))

    if opcao == 'codificar':
        resultado = codificar_decodificar(texto, deslocamento, 'codificar')
        print(f'O texto codificado é: {resultado}')
    elif opcao == 'decodificar':
        resultado = codificar_decodificar(texto, deslocamento, 'decodificar')
        print(f'O texto decodificado é: {resultado}')
    else:
        print('Escolha entre codificar ou decodificar.')
