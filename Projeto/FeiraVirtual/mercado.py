class Mercado:
    # Construtor da classe Mercado, inicializa a lista de artigos do mercado
    def __init__(self):
        self.artigos = []

    # Adiciona um novo artigo ao mercado ou atualiza um existente
    def adicionar_artigo(self, artigo):
        # Procura por um artigo existente com o mesmo nome
        artigo_existente = next((a for a in self.artigos if a.nome == artigo.nome), None)
        
        # Se o artigo já existe, atualiza a quantidade e ajusta o preço
        if artigo_existente:
            artigo_existente.quantidade += artigo.quantidade
            self.ajustar_preco_artigo(artigo_existente)
        else:
            # Se o artigo é novo, adiciona-o ao mercado e ajusta o preço
            self.artigos.append(artigo)
            self.ajustar_preco_artigo(artigo)

    # Ajusta o preço de um artigo com base na quantidade disponível
    def ajustar_preco_artigo(self, artigo):
        # Aumenta o preço em 25% se a quantidade é menor ou igual a 3
        if artigo.quantidade <= 3:
            artigo.preco *= 1.25
        # Reduz o preço em 25% se a quantidade é maior que 10
        elif artigo.quantidade > 10:
            artigo.preco *= 0.75
        
    # Remove um artigo do mercado
    def remover_artigo(self, artigo_nome):
        # Filtra os artigos mantendo todos exceto o que tem o nome especificado
        self.artigos = [artigo for artigo in self.artigos if artigo.nome != artigo_nome]

    # Mostra detalhes de um artigo específico
    def mostrar_artigo(self, artigo):
        # Verifica se há artigos disponíveis
        if not self.artigos:
            return "Nenhum artigo disponível."
        artigos_formatados = []
        # Formata a apresentação de cada artigo
        for artigo in self.artigos:
            artigo_str = f"Nome: {artigo.nome}, Preço: {artigo.preco}, Tipologia: {artigo.tipologia}, Quantidade: {artigo.quantidade}"
            artigos_formatados.append(artigo_str)

        return '\n'.join(artigos_formatados)
