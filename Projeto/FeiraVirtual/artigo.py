class Artigo:
    # Construtor da classe Artigo, inicializa um novo artigo com nome, preço, tipologia e quantidade
    def __init__(self, nome, preco, tipologia, quantidade):
        self.nome = nome  # Nome do artigo
        self.preco = preco  # Preço do artigo
        self.tipologia = tipologia  # Tipo ou categoria do artigo
        self.quantidade = quantidade  # Quantidade disponível do artigo

    # Aplica regras de preço com base na quantidade disponível
    def aplicar_regras_preco(self):
        # Aumenta o preço em 25% se a quantidade for menor ou igual a 3
        if self.quantidade <= 3:
            self.preco *= 1.25
        # Reduz o preço em 25% se a quantidade for maior que 10
        elif self.quantidade > 10:
            self.preco *= 0.75

    # Permite editar o nome do artigo
    def editar_nome(self, nome):
        self.nome = nome  # Atualiza o nome do artigo

    # Ajusta o preço do artigo com base em uma percentagem de alteração
    def ajustar_preco(self, percentagem_alteracao):
        # Ajusta o preço de acordo com a percentagem fornecida
        self.preco *= (1 + percentagem_alteracao / 100)

    # Altera o preço do artigo diretamente com o novo valor fornecido
    def editar_preco(self, preco):
        self.preco = preco  # Atualiza o preço do artigo
        # Aplica as regras de preço com base na quantidade disponível
        self.aplicar_regras_preco()

    # Retorna o preço atual do artigo
    def mostrar_preco(self):
        return self.preco

    # Altera a quantidade do artigo
    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade  # Atualiza a quantidade do artigo

    # Retorna a quantidade atual do artigo
    def mostrar_quantidade(self):
        return self.quantidade

    # Altera a tipologia do artigo
    def editar_tipo(self, novo_tipo):
        self.tipologia = novo_tipo  # Atualiza a tipologia do artigo

    # Retorna a tipologia atual do artigo
    def mostrar_tipo(self):
        return self.tipologia
