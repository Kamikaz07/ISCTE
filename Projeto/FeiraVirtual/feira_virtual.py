from utilizador import Utilizador
from artigo import Artigo
from mercado import Mercado


class FeiraVirtual:
    def __init__(self):
        self.utilizadores = {}
        self.mercado = Mercado()
        
    def criar_novo_artigo(self, nome_utilizador):
        nome_artigo = input("Nome do novo artigo: ")
        preco_artigo = float(input("Preço do artigo: "))
        tipologia_artigo = input("Tipologia do artigo: ")
        quantidade_artigo = int(input("Quantidade do artigo: "))

        novo_artigo = Artigo(nome_artigo, preco_artigo, tipologia_artigo, quantidade_artigo)
        self.utilizadores[nome_utilizador].artigos_disponiveis.append(novo_artigo)
        print(f"Artigo '{nome_artigo}' adicionado com sucesso ao utilizador {nome_utilizador}.")

     
    #Adiciona um novo utilizador recebendo o nome, interesses e artigos    
    def registar_utilizador(self, nome, interesses, artigos_disponiveis, perguntar_artigos=True):
        if nome not in self.utilizadores:
            self.utilizadores[nome] = Utilizador(nome, interesses, artigos_disponiveis)

            if perguntar_artigos:
                # Perguntar se o utilizador quer adicionar um novo artigo
                adicionar_artigo = input(f"Deseja adicionar um artigo para o utilizador {nome}? (s/n): ")
                while adicionar_artigo.lower() == 's':
                    nome_artigo = input("Nome do artigo: ")
                    preco_artigo = float(input("Preço do artigo: "))
                    tipologia_artigo = input("Tipologia do artigo: ")
                    quantidade_artigo = int(input("Quantidade do artigo: "))

                    novo_artigo = Artigo(nome_artigo, preco_artigo, tipologia_artigo, quantidade_artigo)
                    self.utilizadores[nome].artigos_disponiveis.append(novo_artigo)

                    adicionar_artigo = input("Deseja adicionar outro artigo? (s/n): ")
        else:
            raise Exception(f"Utilizador {nome} já existe.")
    
    #Importa uma lista de avaliações a partir de um ficheiro    
    def importar_avaliacoes(self, nome_ficheiro):
        with open(nome_ficheiro, "r", encoding='utf-8') as file:  
            for linha in file:

                partes = linha.strip().split(';')
                if len(partes) == 2 and partes[0] in self.utilizadores:
                    nome, avaliacoes_brutas = partes
                    avaliacoes = FeiraVirtual.processar_avaliacoes(avaliacoes_brutas.strip('[]'))
                    self.utilizadores[nome].avaliacoes = avaliacoes

    def importar_utilizadores(self, nome_ficheiro):
        with open(nome_ficheiro, "r") as file:
            for line in file:
                nome, interesses, artigos_brutos = self.processar_linha(line.strip())
                artigos = self.criar_artigos(artigos_brutos)
                self.registar_utilizador(nome, interesses, artigos, perguntar_artigos=False)

                for artigo in artigos:
                    # Adiciona cada artigo ao mercado com o ajuste de preço aplicado
                    self.mercado.adicionar_artigo(artigo)

                        
    def processar_linha(self, linha):
        # Dividir a linha em nome e o restante
        partes = linha.split('[')
        nome = partes[0].strip(';')
        
        # Verificar se existem interesses e artigos
        if len(partes) > 1:
            interesses = partes[1].strip('];').split(',')
            artigos_brutos = partes[2].strip(']').split(';') if len(partes) > 2 else []
        else:
            interesses = []
            artigos_brutos = []

        return nome, interesses, artigos_brutos
    
    #Elimina um utilizador 
    def eliminar_conta(self, nome_utilizador):
        if nome_utilizador in self.utilizadores:
            del self.utilizadores[nome_utilizador]
        else:
            raise Exception(f"Utilizador {nome_utilizador} não encontrado.")
        
    #Apresenta todos os artigos disponíveis ordenados por preço     
    def listar_artigos(self):
        if not self.mercado.artigos:
            return "Nenhum artigo disponível no mercado."

        artigos_agrupados = {}
        for nome, utilizador in self.utilizadores.items():
            for artigo in utilizador.artigos_disponiveis:
                if artigo.nome not in artigos_agrupados:
                    artigos_agrupados[artigo.nome] = {'quantidade': 0, 'preco_total': 0.0}
                artigos_agrupados[artigo.nome]['quantidade'] += artigo.quantidade
                artigos_agrupados[artigo.nome]['preco_total'] += artigo.preco * artigo.quantidade

        artigos_formatados = []
        for nome, dados in artigos_agrupados.items():
            preco_medio = dados['preco_total'] / dados['quantidade']
            artigos_formatados.append(f"Nome: {nome}, Preço Médio: {preco_medio:.2f}, Quantidade Total: {dados['quantidade']}")

        return '\n'.join(artigos_formatados)
    
    #Efetua uma compra de um artigo. O comprador e o vendedor são os nomes de dois utilizadores registados 
    def comprar_artigo(self, comprador, vendedor, artigo_nome, quantidade):
        if comprador in self.utilizadores and vendedor in self.utilizadores:
            comprador_obj = self.utilizadores[comprador]
            vendedor_obj = self.utilizadores[vendedor]

            # Encontrar o artigo no mercado para usar o preço de lá
            artigo_mercado = next((a for a in self.mercado.artigos if a.nome == artigo_nome), None)
            
            if artigo_mercado and quantidade <= artigo_mercado.quantidade:
                custo_total = artigo_mercado.preco * quantidade

                if comprador_obj.pycoins >= custo_total:
                    comprador_obj.pycoins -= custo_total
                    vendedor_obj.pycoins += custo_total

                    artigo_mercado.quantidade -= quantidade
                    if artigo_mercado.quantidade == 0:
                        self.mercado.artigos.remove(artigo_mercado)

                    # Adicionar artigo ao inventário do comprador
                    artigo_comprado = next((a for a in comprador_obj.artigos_disponiveis if a.nome == artigo_nome), None)
                    if artigo_comprado:
                        artigo_comprado.quantidade += quantidade
                    else:
                        novo_artigo = Artigo(artigo_nome, artigo_mercado.preco, artigo_mercado.tipologia, quantidade)
                        comprador_obj.artigos_disponiveis.append(novo_artigo)

                    print(f"Compra de '{quantidade}x {artigo_nome}' realizada com sucesso por {comprador} de {vendedor}.")

                    # Solicitar avaliação do vendedor
                    estrelas = int(input(f"Avalie o vendedor {vendedor} (1 a 5 estrelas): "))
                    comentario = input("Deixe um comentário: ")
                    vendedor_obj.deixar_avaliacao(estrelas, comentario)

                else:
                    raise Exception("Saldo insuficiente para realizar a compra.")
            else:
                raise Exception("Quantidade insuficiente ou artigo não encontrado no mercado.")
        else:
            raise Exception("Comprador ou vendedor não encontrado.")
    
    #Calcula a reputação de um utilizador com base nas suas avaliações    
    def calcular_reputacao(self, utilizador):
        if not utilizador.avaliacoes:
            return 0
        total_estrelas = sum(estrelas for estrelas, _ in utilizador.avaliacoes)
        return total_estrelas / len(utilizador.avaliacoes)
    
    #Coloca um artigo à venda. O vendedor é o nome de um utilizador     
    def colocar_artigo_para_venda(self, vendedor, nome_artigo, preco, quantidade):
        if vendedor not in self.utilizadores:
            return "Vendedor não encontrado."

        # Procura o artigo no mercado
        artigo_existente = self.mercado.encontrar_artigo(nome_artigo)

        if artigo_existente:
            # Atualiza o preço para o menor valor e ajusta a quantidade
            artigo_existente.preco = min(artigo_existente.preco, preco)
            artigo_existente.quantidade += quantidade
        else:
            # Cria um novo artigo e o adiciona ao mercado
            novo_artigo = Artigo(nome_artigo, preco, "Desconhecida", quantidade)
            self.mercado.adicionar_artigo(novo_artigo)
            artigo_existente = novo_artigo

        # Atualiza o preço e a quantidade do artigo com base nas regras
        if artigo_existente.quantidade <= 3:
            artigo_existente.preco *= 1.25
        elif artigo_existente.quantidade > 10:
            artigo_existente.preco *= 0.75

        # Atualiza os artigos do vendedor
        artigo_vendedor = next((a for a in self.utilizadores[vendedor].artigos_disponiveis if a.nome == nome_artigo), None)
        if artigo_vendedor:
            artigo_vendedor.quantidade += quantidade
            artigo_vendedor.preco = artigo_existente.preco
        else:
            novo_artigo_vendedor = Artigo(nome_artigo, artigo_existente.preco, "Desconhecida", quantidade)
            self.utilizadores[vendedor].artigos_disponiveis.append(novo_artigo_vendedor)

        return f"Artigo '{nome_artigo}' colocado à venda por {vendedor}."
    
    #Encontra os nomes de utilizadores interessados no artigo recebido     
    def encontrar_compradores_interessados(self, tipologia):
        possiveis_compradores = []
        for nome, utilizador in self.utilizadores.items():
            if tipologia in utilizador.interesses:
                possiveis_compradores.append(nome)
        return possiveis_compradores

    def encontrar_artigo(self, nome_artigo):
        for artigo in self.mercado.artigos:
            if artigo.nome == nome_artigo:
                return artigo
        return None
    
    #Exporta a lista de artigos para um ficheiro ordenados por quantidade 
    def exportar_artigos_preco(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            for artigo in self.mercado.artigos:
                linha = f"{artigo.nome},{artigo.preco},{artigo.tipologia},{artigo.quantidade}\n"
                file.write(linha)

    def exportar_avaliacoes(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            for nome, utilizador in self.utilizadores.items():
                avaliacoes = ';'.join([f"{estrelas},{comentario}" for estrelas, comentario in utilizador.avaliacoes])
                file.write(f"{nome};[{avaliacoes}]\n")
                
    @staticmethod
    def processar_avaliacoes(avaliacoes_brutas):
        avaliacoes = []
        avaliacoes_split = avaliacoes_brutas.split('],[')
        for avaliacao in avaliacoes_split:
            avaliacao = avaliacao.replace('[', '').replace(']', '')
            if avaliacao:  # Certifica-se de que a avaliação não está vazia
                estrelas, comentario = avaliacao.split(',', 1)
                avaliacoes.append((int(estrelas), comentario.strip()))
        return avaliacoes

    

    def criar_artigos(self, artigos_brutos):
        artigos = []
        for artigo_str in artigos_brutos:
            if artigo_str:
                dados_artigo = artigo_str.split(',')
                # Garantir que temos 4 partes: nome, preco, tipologia, quantidade
                if len(dados_artigo) == 4:
                    nome_artigo, preco, tipologia, quantidade = dados_artigo
                    # Convertendo preço para float e quantidade para int
                    try:
                        preco = float(preco.strip())
                        quantidade = int(quantidade.strip())
                    except ValueError:
                        # Se ocorrer um erro na conversão, pular este artigo
                        continue

                    artigos.append(Artigo(nome_artigo.strip(), preco, tipologia.strip(), quantidade))
        return artigos
    
    def listar_vendedores_por_reputacao(self, nome_artigo):
        vendedores = []

        for nome, utilizador in self.utilizadores.items():
            for artigo in utilizador.artigos_disponiveis:
                if artigo.nome == nome_artigo:
                    reputacao = self.calcular_reputacao(utilizador)
                    vendedores.append((nome, reputacao, artigo.preco))

        # Ordena os vendedores por reputação
        vendedores_ordenados = sorted(vendedores, key=lambda x: x[1], reverse=True)

        # Exibe a lista de vendedores ordenada, incluindo os preços
        print("\nVendedores disponíveis para este artigo:")
        for vendedor, reputacao, preco in vendedores_ordenados:
            print(f"Vendedor: {vendedor}, Reputação: {reputacao:.2f} estrelas, Preço: {preco} Pycoins")

            
    def mostrar_todos_artigos(self):
        todos_artigos_str = []
        for nome, utilizador in self.utilizadores.items():
            artigos_utilizador = utilizador.mostrar_artigos()
            if artigos_utilizador != "Nenhum artigo disponível.":
                todos_artigos_str.append(f"Artigos do Utilizador {nome}:\n{artigos_utilizador}")
            else:
                todos_artigos_str.append(f"Utilizador {nome} não tem artigos disponíveis.")
        return '\n\n'.join(todos_artigos_str)

    def remover_artigo_mercado_utilizadores(self, nome_artigo):
        # Remove o artigo do mercado
        self.mercado.remover_artigo(nome_artigo)

        # Remove ou atualiza o artigo dos utilizadores
        for utilizador in self.utilizadores.values():
            utilizador.artigos_disponiveis = [artigo for artigo in utilizador.artigos_disponiveis if artigo.nome != nome_artigo]