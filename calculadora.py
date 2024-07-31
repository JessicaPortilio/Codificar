def adicao(num1, num2):
    return num1 + num2  # Função para somar dois números

def subtracao(num1, num2):
    return num1 - num2  # Função para subtrair o segundo número do primeiro

def multiplicacao(num1, num2):
    return num1 * num2  # Função para multiplicar dois números

def divisao(num1, num2):
    if num2 == 0:
        raise ValueError("Não é possível dividir por zero.")  # Verifica se o divisor é zero e gera um erro se for o caso
    return num1 / num2  # Função para dividir o primeiro número pelo segundo

# Dicionário que associa operadores a suas funções correspondentes
operacoes = {
    '+': adicao,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}

def mostrar_opcoes(operacoes):
    # Função que imprime as operações disponíveis
    print("Operações disponíveis:")
    for operacao in operacoes.keys():
        print(operacao)  # Imprime cada operador disponível

def solicitar_numero(mensagem):
    # Função que solicita um número do usuário e garante que a entrada seja válida
    while True:
        try:
            return float(input(mensagem))  # Solicita e retorna um número float do usuário
        except ValueError:
            print("Por favor, insira um número válido.")  # Mensagem de erro se a entrada não for um número válido

def solicitar_operacao():
    # Função que solicita a operação desejada do usuário e garante que a entrada seja válida
    while True:
        mostrar_opcoes(operacoes)  # Mostra as operações disponíveis
        operador = input('Qual operação deseja realizar: ')  # Solicita ao usuário que escolha uma operação
        if operador in operacoes:
            return operador  # Retorna o operador escolhido se for válido
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")  # Mensagem de erro se a entrada não for um operador válido

def calcular():
    # Função principal que executa a calculadora
    num1 = solicitar_numero('Informe o primeiro número: ')  # Solicita o primeiro número do usuário
    while True:
        operador = solicitar_operacao()  # Solicita a operação desejada
        num2 = solicitar_numero('Informe o segundo número: ')  # Solicita o segundo número do usuário
        try:
            resultado = operacoes[operador](num1, num2)  # Calcula o resultado usando a operação escolhida
            if isinstance(resultado, int) or resultado.is_integer():
                print(f'{num1} {operador} {num2} = {int(resultado)}')  # Imprime o resultado como inteiro se não tiver parte decimal
            else:
                print(f'{num1} {operador} {num2} = {resultado:.2f}')  # Imprime o resultado com duas casas decimais se for um float
        except ValueError as e:
            print(e)  # Imprime a mensagem de erro se houver um erro na operação (ex: divisão por zero)
            continue

        opcao = input(f'Digite [S]im para continuar com o {resultado} ou [N]ão para sair: ').strip().lower()
        # Solicita ao usuário se deseja continuar com o resultado ou sair
        if opcao == 'n':
            break  # Encerra o loop se o usuário escolher 'n'
        num1 = resultado  # Atualiza o primeiro número com o resultado para a próxima operação

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    calcular()  # Chama a função principal para iniciar a calculadora
