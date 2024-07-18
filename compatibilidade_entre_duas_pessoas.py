# Função para calcular a pontuação do amor
def calcular_pontuacao(nome1, nome2):
    # Converte os nomes para minúsculas
    nome1 = nome1.lower()
    nome2 = nome2.lower()
    
    # Combina os nomes em uma única string
    combinado = nome1 + nome2
    
    # Conta as ocorrências das letras em "TRUE"
    v = combinado.count('v')
    e = combinado.count('e')
    r = combinado.count('r')
    d = combinado.count('d')
    a = combinado.count('a')
    d = combinado.count('d')
    e = combinado.count('e')
    true_total = v + e + r + d + a + d + e
    
    # Conta as ocorrências das letras em "LOVE"
    a = combinado.count('a')
    m = combinado.count('m')
    o = combinado.count('o')
    r = combinado.count('r')
    love_total = a + m + o + r
    
    # Combina os totais para formar a pontuação do amor
    pontuacao = int(str(true_total) + str(love_total))
    
    return pontuacao

# Função principal para o programa
def calculadora_do_amor():
    print("Bem-vindo à Calculadora do Amor!")
    nome1 = input("Qual é o seu nome? ")
    nome2 = input("Qual é o nome da outra pessoa? ")
    
    pontuacao = calcular_pontuacao(nome1, nome2)
    
    print("A Calculadora do Amor está calculando sua pontuação...")
    
    # Determina a mensagem com base na pontuação
    if pontuacao < 10 or pontuacao > 90:
        print(f"Sua pontuação é {pontuacao}, vocês combinam como coca e mentos.")
    elif 40 <= pontuacao <= 50:
        print(f"Sua pontuação é {pontuacao}, vocês são bons juntos.")
    else:
        print(f"Sua pontuação é {pontuacao}.")
    
# Chama a função principal para executar o programa
calculadora_do_amor()
