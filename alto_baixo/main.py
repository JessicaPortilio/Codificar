import requests  # Importa a biblioteca requests para fazer requisições HTTP
import random  # Importa a biblioteca random para gerar valores aleatórios

LOGO = r'''
  ____        _        _ _                 _             ______     _            _           
 |  _ \      | |      | | |               | |           |  ____|   | |          | |          
 | |_) | __ _| |_ __ _| | |__   __ _    __| | __ _ ___  | |__   ___| |_ _ __ ___| | __ _ ___ 
 |  _ < / _` | __/ _` | | '_ \ / _` |  / _` |/ _` / __| |  __| / __| __| '__/ _ \ |/ _` / __|
 | |_) | (_| | || (_| | | | | | (_| | | (_| | (_| \__ \ | |____\__ \ |_| | |  __/ | (_| \__ \
 |____/ \__,_|\__\__,_|_|_| |_|\__,_|  \__,_|\__,_|___/ |______|___/\__|_|  \___|_|\__,_|___/
                                                                                             
'''

def acessar_informacao_artista(nome_artista):
    """Acessa a URL para obter os dados do artista no Vagalume"""
    URL = f"https://www.vagalume.com.br/{nome_artista}/index.js"  # Cria a URL do artista no Vagalume
    response = requests.get(URL)  # Faz uma requisição HTTP para obter os dados do artista
    return response.json()  # Retorna os dados do artista em formato JSON

def gerar_aleatoriamente(lista_nomes):
    """Gera um nome aleatório da lista fornecida"""
    nome = random.choice(lista_nomes)  # Seleciona um nome aleatório da lista
    return nome  # Retorna o nome selecionado

def verificar_rank(informacao_do_artista1, informacao_do_artista2):
    """Verifica qual artista tem a maior pontuação"""
    pontos1 = float(informacao_do_artista1["artist"]["rank"]["points"])  # Obtém a pontuação do primeiro artista
    pontos2 = float(informacao_do_artista2["artist"]["rank"]["points"])  # Obtém a pontuação do segundo artista
    return informacao_do_artista1["artist"]["desc"] if pontos1 > pontos2 else informacao_do_artista2["artist"]["desc"]  
    # Retorna o nome do artista com a maior pontuação

def play():
    """Função principal para execução do jogo"""
    # Lista de nomes de artistas
    lista_de_nomes_de_artistas = ['taylor-swift', 'u2', 'coldplay', 'rihanna', 
                                'beyonce', 'katy-perry', 'lady-gaga', 'shakira', 
                                'ariana-grande', 'adele', 'lana-del-rey']
    
    # Escolher um primeiro artista inicial
    nome_artista1 = gerar_aleatoriamente(lista_de_nomes_de_artistas)  # Gera um nome aleatório da lista
    lista_de_nomes_de_artistas.remove(nome_artista1)  # Remove o nome gerado da lista para evitar repetição
    informacao_do_artista1 = acessar_informacao_artista(nome_artista1)  # Obtém informações do artista escolhido
    
    # Loop principal do jogo que continua enquanto houver artistas na lista
    while lista_de_nomes_de_artistas:
        # Escolher um segundo artista aleatoriamente
        nome_artista2 = gerar_aleatoriamente(lista_de_nomes_de_artistas)  # Gera outro nome aleatório
        lista_de_nomes_de_artistas.remove(nome_artista2)  # Remove o segundo nome gerado da lista
        informacao_do_artista2 = acessar_informacao_artista(nome_artista2)  # Obtém informações do segundo artista
        
        # Verificar qual artista realmente tem a maior pontuação
        resultado = verificar_rank(informacao_do_artista1, informacao_do_artista2)  # Compara as pontuações dos dois artistas

        # Alternar a ordem dos artistas aleatoriamente
        if random.choice([True, False]):  # Decide aleatoriamente a ordem de exibição dos artistas
            nome1, pontos1 = informacao_do_artista1['artist']['desc'], informacao_do_artista1["artist"]["rank"]["points"]  
            # Define nome1 e pontos1 como o primeiro artista
            nome2, pontos2 = informacao_do_artista2['artist']['desc'], informacao_do_artista2["artist"]["rank"]["points"]  
            # Define nome2 e pontos2 como o segundo artista
        else:
            nome1, pontos1 = informacao_do_artista2['artist']['desc'], informacao_do_artista2["artist"]["rank"]["points"]  
            # Define nome1 e pontos1 como o segundo artista
            nome2, pontos2 = informacao_do_artista1['artist']['desc'], informacao_do_artista1["artist"]["rank"]["points"]  
            # Define nome2 e pontos2 como o primeiro artista
        
        # Exibir os artistas e suas pontuações (apenas para depuração)
        print(nome1, pontos1)
        print(nome2, pontos2)
        
        # Perguntar ao usuário qual artista tem a maior pontuação
        print(f'Qual artista tem a maior pontuação?\n1. {nome1}\n2. {nome2}')
        opcao = input('Digite o número do artista que você acha que tem a maior pontuação: ')  # Recebe a escolha do usuário
        
        # Verificar qual artista o usuário escolheu
        escolha_usuario = nome1 if opcao == '1' else nome2  # Define a escolha do usuário

        # Mostrar resultado ao usuário
        if escolha_usuario == resultado:  # Verifica se o usuário escolheu corretamente
            print(f'Você acertou! {resultado} tem a maior pontuação.')
        else:
            print(f'Você errou. {resultado} tem a maior pontuação.')
            return  # Se o usuário errar, o jogo termina
        
        # Atualizar para a próxima rodada
        if resultado == informacao_do_artista1['artist']['desc']:  # Mantém o vencedor da rodada anterior
            informacao_do_artista1 = informacao_do_artista1  # Mantém as informações do artista vencedor
        else:
            informacao_do_artista1 = informacao_do_artista2  # Atualiza com as informações do novo vencedor
    print('PARABÉNS!!! Você aceitou todos!!!')   
if __name__ == "__main__":
    print(LOGO)
    play()
        
