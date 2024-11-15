import requests  # Importa a biblioteca para fazer requisições HTTP.
import random  # Importa a biblioteca para gerar números aleatórios.
from tkinter import Tk, Label, Button, Frame, messagebox  # Importa classes do Tkinter para criar a interface gráfica.
from io import BytesIO  # Importa BytesIO para ler imagens em formato binário.
from PIL import Image, ImageTk  # Importa a biblioteca PIL para manipulação de imagens e Tkinter para exibir imagens no Tkinter.

# Função para acessar informações sobre um artista usando a API do Vagalume.
def acessar_informacao_artista(nome_artista):
    """Acessa a URL para obter os dados do artista no Vagalume"""
    URL = f"https://www.vagalume.com.br/{nome_artista}/index.js"  # Cria a URL para acessar as informações do artista.
    response = requests.get(URL)  # Faz uma requisição HTTP para obter os dados.
    return response.json()  # Retorna os dados em formato JSON.

# Função para escolher aleatoriamente um nome de artista de uma lista.
def gerar_aleatoriamente(lista_nomes):
    """Gera um nome aleatório da lista fornecida"""
    return random.choice(lista_nomes)  # Retorna um nome de artista aleatório da lista.

# Função para comparar a pontuação entre dois artistas e retornar o artista com a maior pontuação.
def verificar_rank(info_artista1, info_artista2):
    """Verifica qual artista tem a maior pontuação"""
    pontos1 = float(info_artista1["artist"]["rank"]["points"])  # Obtém a pontuação do primeiro artista.
    pontos2 = float(info_artista2["artist"]["rank"]["points"])  # Obtém a pontuação do segundo artista.
    print(info_artista1["artist"]["desc"], pontos1, '-', info_artista2["artist"]["desc"], pontos2)
    return info_artista1["artist"]["desc"] if pontos1 > pontos2 else info_artista2["artist"]["desc"]  # Retorna o artista com a maior pontuação.


# Classe principal do jogo.
class ArtistaGame:
    def __init__(self, root):
        self.root = root  # Armazena a janela principal.
        self.root.title("Batalha das Estrelas")  # Define o título da janela.
        self.root.geometry("700x500")  # Define o tamanho da janela.
        self.root.config(bg='#d6d4d4')
        # Lista de nomes de artistas.
        self.lista_de_nomes_de_artistas = [
            'taylor-swift', 'u2', 'coldplay', 'rihanna', 
            'katy-perry', 'lady-gaga', 'shakira', 
            'ariana-grande', 'adele', 'lana-del-rey'
        ]
        
        self.pontuacao = 0  # Inicializa a pontuação do jogador.
        self.max_rodadas = 9  # Define o número máximo de rodadas.
        self.rodadas_restantes = self.max_rodadas  # Define o número de rodadas restantes.
        self.jogo_terminado = False  # Define se o jogo terminou ou não.

        # Seleciona aleatoriamente o primeiro artista e obtém suas informações.
        self.nome_artista1 = gerar_aleatoriamente(self.lista_de_nomes_de_artistas)  # Gera um nome aleatório da lista
        self.lista_de_nomes_de_artistas.remove(self.nome_artista1)  # Remove o nome gerado da lista para evitar repetição
        self.informacao_do_artista1 = acessar_informacao_artista(self.nome_artista1)  # Obtém informações do artista escolhido
        
        # Cria e configura o título da janela.
        self.label_title = Label(root, text='Batalha das Estrelas', font=("Simplified Arabic", 45, 'italic'), bg='#d6d4d4')
        self.label_title.pack(pady=5)
        
        # Criar um frame para os artistas.
        self.frame_artistas = Frame(root, background='#d6d4d4')
        self.frame_artistas.pack(pady=5)
        
        # Cria frame para cada artista e os posiciona
        self.frame_artista1 = Frame(self.frame_artistas, background='#d6d4d4')
        self.frame_artista1.pack(side="left", padx=20)
        
        self.frame_artista2 = Frame(self.frame_artistas, background='#d6d4d4')
        self.frame_artista2.pack(side="right", padx=20)
        
        # Cria e configura a label para o nome e imagem do primeiro artista.
        self.label_nome1 = Label(self.frame_artista1, text="", font=("Cambria", 18, 'bold'), bg='#d6d4d4')
        self.label_nome1.pack(pady=10)
        
        self.label_img1 = Label(self.frame_artista1)
        self.label_img1.pack()
        
        # Cria o botão para escolher o primeiro artista.
        self.botao_artista1 = Button(self.frame_artista1, text="Escolher", command=lambda: self.verificar_escolha(self.label_nome1['text']), bg='#252d54', fg='white')
        self.botao_artista1.pack(pady=10)
        
        # Cria e configura a label para o nome e imagem do segundo artista.
        self.label_nome2 = Label(self.frame_artista2, text="", font=("Cambria", 18, 'bold'), bg='#d6d4d4')
        self.label_nome2.pack(pady=10)

        self.label_img2 = Label(self.frame_artista2)
        self.label_img2.pack()

        # Cria o botão para escolher o segundo artista.
        self.botao_artista2 = Button(self.frame_artista2, text="Escolher", command=lambda: self.verificar_escolha(self.label_nome2['text']), bg='#252d54', fg='white')
        self.botao_artista2.pack(pady=10)
        
        # Criar label para exibir o resultado, pontuação e rodadas restantes
        # Criar um frame para os artistas.
        self.frame_resultados = Frame(root, background='#d6d4d4')
        self.frame_resultados.pack(pady=5)
        
        # Cria e configura as labels para exibir o resultado, pontuação e rodadas restantes.
        self.label_resultado = Label(self.frame_resultados, text="", font=("Arial", 18), bg='#d6d4d4')
        self.label_resultado.grid(row=0, column=0, padx=5, pady=5)
        
        self.frame_pontuacao = Frame(root, background='#d6d4d4')
        self.frame_pontuacao.pack(pady=5)
        
        self.label_pontuacao = Label(self.frame_pontuacao, text=f"Pontuação: {self.pontuacao}", font=("Arial", 16), bg='#d6d4d4')
        self.label_pontuacao.grid(row=1, column=0, padx=5, pady=5)
        
        self.label_rodadas = Label(self.frame_pontuacao, text=f"Rodadas restantes: {self.rodadas_restantes - 1}", font=("Arial", 16), bg='#d6d4d4')
        self.label_rodadas.grid(row=1, column=1, padx=5, pady=5)
        
        self.proxima_rodada()  # Inicia a primeira rodada do jogo.
    
    # Função para obter a imagem de um artista.
    def obter_imagem_artista(self, nome_artista):
        URL = f"https://www.vagalume.com.br/{nome_artista}/images/profile.jpg"  # Cria a URL para acessar a imagem do artista.
        response = requests.get(URL)  # Faz uma requisição HTTP para obter a imagem.
        
        if response.status_code != 200:  # Verifica se houve erro ao obter a imagem.
            print(f"Erro ao obter imagem para {nome_artista}: Código de status {response.status_code}")
            return None
        
        img_data = response.content  # Obtém os dados da imagem.
        
        try:
            image = Image.open(BytesIO(img_data))  # Abre a imagem usando PIL.
            image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensiona a imagem.
            return ImageTk.PhotoImage(image)  # Converte a imagem para o formato Tkinter.
        except Exception as e:
            print(f"Erro ao processar a imagem para {nome_artista}: {e}")
            return None
        
    # Função para avançar para a próxima rodada.
    def proxima_rodada(self):
        if self.jogo_terminado:  # Verifica se o jogo terminou.
            return
        # print(self.lista_de_nomes_de_artistas)
        # print(self.rodadas_restantes)
        self.label_rodadas.config(text=f"Rodadas restantes: {self.rodadas_restantes}",)  # Atualiza a label de rodadas restantes.
        # if not self.lista_de_nomes_de_artistas:
        #     messagebox.showwarning('Aviso', 'Terminou a lista de artitas!!!')
            
        if not self.lista_de_nomes_de_artistas or self.rodadas_restantes == 0:  # Verifica se ainda há rodadas restantes.
            self.jogo_terminado = True  # Marca o jogo como terminado.
            self.label_resultado.config(text=f"Fim do jogo! Sua pontuação final é: {self.pontuacao}")  # Exibe a pontuação final.
            return
        

        
        # Seleciona aleatoriamente o segundo artista e obtém suas informações.
        self.nome_artista2 = gerar_aleatoriamente(self.lista_de_nomes_de_artistas)  # Gera outro nome aleatório
        self.lista_de_nomes_de_artistas.remove(self.nome_artista2)  # Remove o segundo nome gerado da lista
        self.informacao_do_artista2 = acessar_informacao_artista(self.nome_artista2)  # Obtém informações do segundo artista
        
        # Alterna entre os artistas na tela para criar variedade.
        if random.choice([True, False]):  # Decide aleatoriamente a ordem de exibição dos artistas
            self.nome1, self.pontos1 = self.informacao_do_artista1['artist']['desc'], self.informacao_do_artista1["artist"]["rank"]["points"]
            self.nome2, self.pontos2 = self.informacao_do_artista2['artist']['desc'], self.informacao_do_artista2["artist"]["rank"]["points"]
        else:
            self.nome1, self.pontos1 = self.informacao_do_artista2['artist']['desc'], self.informacao_do_artista2["artist"]["rank"]["points"]
            self.nome2, self.pontos2 = self.informacao_do_artista1['artist']['desc'], self.informacao_do_artista1["artist"]["rank"]["points"]
        
        self.label_nome1.config(text=self.nome1)  # Atualiza o nome do primeiro artista na tela.
        self.label_nome2.config(text=self.nome2)  # Atualiza o nome do segundo artista na tela.
        
        img1 = self.obter_imagem_artista(self.nome1.replace(' ', '-').lower())  # Obtém a imagem do primeiro artista.
        img2 = self.obter_imagem_artista(self.nome2.replace(' ', '-').lower())  # Obtém a imagem do segundo artista.
        
        if img1:  # Verifica se a imagem do primeiro artista foi carregada com sucesso.
            self.label_img1.config(image=img1)  # Atualiza a imagem do primeiro artista na tela.
            self.label_img1.image = img1  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector.

        if img2:  # Verifica se a imagem do segundo artista foi carregada com sucesso.
            self.label_img2.config(image=img2)  # Atualiza a imagem do segundo artista na tela.
            self.label_img2.image = img2  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector.
        
        #self.rodadas_restantes -= 1  # Decrementa o número de rodadas restantes.
        #rodadas = self.rodadas_restantes  if self.rodadas_restantes == 0 else self.rodadas_restantes + 1
        
    
    # Função para verificar a escolha do usuário.
    def verificar_escolha(self, escolha_usuario):
        if self.jogo_terminado: # Verifica se o jogo terminou.
            messagebox.showinfo('Fim do Jogo', 'O jogo já terminou. Não é possível fazer mais escolhas.')
            return

        # Verificar qual artista realmente tem a maior pontuação
        resultado = verificar_rank(self.informacao_do_artista1, self.informacao_do_artista2)  # Compara as pontuações dos dois artistas
        
        if escolha_usuario == resultado:  # Verifica se a escolha do usuário está correta.
            self.pontuacao += 1  # Incrementa a pontuação do usuário.
            self.label_pontuacao.config(text=f"Pontuação: {self.pontuacao}")  # Atualiza a label de pontuação.
            self.label_resultado.config(text=f'Você acertou! {resultado} tem a maior pontuação.')  # Exibe uma mensagem informando que a escolha estava correta.
            self.informacao_do_artista1 = self.informacao_do_artista1 if resultado == self.informacao_do_artista1['artist']['desc'] else self.informacao_do_artista2
            self.rodadas_restantes -= 1
            self.proxima_rodada()  # Avança para a próxima rodada.
        else:
            messagebox.showinfo("Errou!", f"Você errou. {resultado} tem a maior pontuação.")  # Exibe uma mensagem informando que a escolha estava incorreta
            self.rodadas_restantes -= 1
            self.proxima_rodada()  # Avança para a próxima rodada.
        
# Código para iniciar o jogo se o arquivo for executado diretamente.
if __name__ == "__main__":
    root = Tk()  # Cria a janela principal do Tkinter.
    game = ArtistaGame(root)  # Cria uma instância do jogo.
    root.mainloop()  # Inicia o loop principal da interface gráfica.
    
    
    
