# Importação da classe Artigo para verificar se um objeto é uma instância de Artigo
from artigo import Artigo

class Utilizador:
    # Construtor da classe Utilizador, inicializa um novo utilizador com nome, interesses, artigos disponíveis, pycoins e avaliações
    def __init__(self, nome, interesses, artigos_disponiveis):
        self.nome = nome  # Nome do utilizador
        self.interesses = interesses  # Interesses do utilizador
        self.artigos_disponiveis = artigos_disponiveis if artigos_disponiveis is not None else []  # Artigos disponíveis
        self.pycoins = 50  # Moeda virtual do sistema, inicializada em 50
        self.avaliacoes = []  # Lista de avaliações recebidas pelo utilizador

    # Permite editar os interesses e os artigos do utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.interesses = novos_interesses  # Atualiza os interesses
        self.artigos_disponiveis = novos_artigos  # Atualiza a lista de artigos disponíveis

    # Adiciona uma nova avaliação ao perfil do utilizador
    def deixar_avaliacao(self, estrelas, comentario):
        self.avaliacoes.append((estrelas, comentario))  # Adiciona um par (estrelas, comentário) à lista de avaliações

    # Calcula a reputação média do utilizador com base nas estrelas das avaliações
    def calcular_reputacao(self):
        if not self.avaliacoes:
            return 0  # Retorna 0 se não houver avaliações
        total_estrelas = sum(estrelas for estrelas, _ in self.avaliacoes)
        return total_estrelas / len(self.avaliacoes)  # Calcula a média de estrelas

    # Exibe todas as avaliações e comentários recebidos pelo utilizador
    def listar_avaliacoes(self):
        reputacao = self.calcular_reputacao()
        print(f"\nUtilizador: {self.nome}")
        print(f"Reputação Média: {reputacao:.2f} estrelas" if reputacao > 0 else "Reputação Média: Sem avaliações")
        if self.avaliacoes:
            print("Comentários:")
            for estrelas, comentario in self.avaliacoes:
                print(f"- {estrelas} estrelas: {comentario}")
        else:
            print("Nenhum comentário disponível.")

    # Retorna a lista de interesses do utilizador
    def mostrar_interesses(self):
        return self.interesses
    
    # Lista todos os artigos disponíveis do utilizador
    def mostrar_artigos(self):
        if not self.artigos_disponiveis:
            return "Nenhum artigo disponível."
        artigos_formatados = []
        for artigo in self.artigos_disponiveis:
            if isinstance(artigo, Artigo):  # Verifica se o objeto é uma instância de Artigo
                artigo_str = f"Nome: {artigo.nome}, Preço: {artigo.preco}, Quantidade: {artigo.quantidade}"
                artigos_formatados.append(artigo_str)
            else:
                artigos_formatados.append("Artigo inválido ou incompleto")
        return '\n'.join(artigos_formatados)

    # Altera o número de pycoins do utilizador
    def alterar_pycoins(self, numero_pycoins):
        self.pycoins = numero_pycoins
        
    # Retorna a quantidade atual de pycoins do utilizador
    def mostrar_pycoins(self):
        return self.pycoins
