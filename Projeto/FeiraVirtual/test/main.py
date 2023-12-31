class Utilizador:
    def __init__(self, nome, interesses, artigos_disponiveis):
        self.nome = nome
        self.interesses = interesses
        self.artigos_disponiveis = artigos_disponiveis if artigos_disponiveis is not None else []
        self.pycoins = 50
        self.avaliacoes = []

    #Altera os interesses e/ou os artigos de um utilizador
    def editar_conta(self, novos_interesses, novos_artigos):
        self.interesses = novos_interesses
        self.artigos_disponiveis = novos_artigos
        
        
    #Adiciona uma nova avaliação, podendo incluir um comentário 
    def deixar_avaliacao(self, estrelas, comentario):
        self.avaliacoes.append((estrelas, comentario))

    def calcular_reputacao(self):
        if not self.avaliacoes:
            return 0
        total_estrelas = sum(estrelas for estrelas, _ in self.avaliacoes)
        return total_estrelas / len(self.avaliacoes)
    
    #Apresenta todas as avaliações e comentários 
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
    
    #Apresenta interesses
    def mostrar_interesses(self):
        return self.interesses
    
    def mostrar_artigos(self):
        if not self.artigos_disponiveis:
            return "Nenhum artigo disponível."
        artigos_formatados = []
        for artigo in self.artigos_disponiveis:
            if isinstance(artigo, Artigo):  # Verifica se é uma instância de Artigo
                artigo_str = f"Nome: {artigo.nome}, Preço: {artigo.preco}, Quantidade: {artigo.quantidade}"
                artigos_formatados.append(artigo_str)
            else:
                artigos_formatados.append("Artigo inválido ou incompleto")
        return '\n'.join(artigos_formatados)

    #Altera o número de pycoins 
    def alterar_pycoins(self, numero_pycoins):
        self.pycoins = numero_pycoins
        
    #Apresenta o número de pycoins 
    def mostrar_pycoins(self):
        return self.pycoins
    
class Artigo:
    def __init__(self, nome, preco, tipologia, quantidade):
        self.nome = nome
        self.preco = preco
        self.tipologia = tipologia
        self.quantidade = quantidade
        
        
    def aplicar_regras_preco(self):
        if self.quantidade <= 3:
            self.preco *= 1.25
        elif self.quantidade > 10:
            self.preco *= 0.75

    #Altera o nome de um artigo para o novo nome recebido
    def editar_nome(self, nome):
        self.nome = nome

    # Implementação da função ajustar_preco
    def ajustar_preco(self, percentagem_alteracao):
        # Esta função ajusta o preço de acordo com a percentagem fornecida
        self.preco *= (1 + percentagem_alteracao / 100)

    # Correção da função editar_preco
    def editar_preco(self, preco):
        # Esta função agora edita o preço diretamente com o valor fornecido
        self.preco = preco
        # Aplica aumento ou redução de preço com base na quantidade
        if self.quantidade <= 3:
            self.preco *= 1.25  # Aumenta o preço em 25%
        elif self.quantidade > 10:
            self.preco *= 0.75  # Reduz o preço em 25%
    
    #Apresenta o preço do artigo
    def mostrar_preco(self):
        return self.preco

    #Altera a quantidade 
    def editar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade
        
    #Apresenta a quantidade do artigo 
    def mostrar_quantidade(self):
        return self.quantidade

    #Altera a tipologia 
    def editar_tipo(self, novo_tipo):
        self.tipologia = novo_tipo
        
    #Apresenta a tipologia do artigo 
    def mostrar_tipo(self):
        return self.tipologia
    
class Mercado:
    def __init__(self):
        self.artigos = []

    def adicionar_artigo(self, artigo):
        artigo_existente = next((a for a in self.artigos if a.nome == artigo.nome), None)
        if artigo_existente:
            artigo_existente.quantidade += artigo.quantidade
            # Chama a função para ajustar o preço
            self.ajustar_preco_artigo(artigo_existente)
        else:
            self.artigos.append(artigo)
            # Ajusta o preço para o novo artigo
            self.ajustar_preco_artigo(artigo)

    def ajustar_preco_artigo(self, artigo):
        if artigo.quantidade <= 3:
            artigo.preco *= 1.25
        elif artigo.quantidade > 10:
            artigo.preco *= 0.75
        
    #Elimina um artigo 
    def remover_artigo(self, artigo_nome):
        self.artigos = [artigo for artigo in self.artigos if artigo.nome != artigo_nome]

        # Retornar None se o artigo não for encontrado
        return None
    
    #Mostra o nome, preço e quantidade do artigo recebido 
    def mostrar_artigo(self, artigo):
        if not self.artigos_disponiveis:
            return "Nenhum artigo disponível."
        artigos_formatados = []
        for artigo in self.artigos_disponiveis:
            artigo_str = f"Nome: {artigo.nome}, Preço: {artigo.preco}, Tipologia: {artigo.tipologia}, Quantidade: {artigo.quantidade}"
            artigos_formatados.append(artigo_str)

        return '\n'.join(artigos_formatados)
    
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

def submenu_utilizadores(feira):
    while True:
        print("\nSubMenu Utilizadores:")
        print("1 - Registrar Utilizador")
        print("2 - Alterar Utilizador")
        print("3 - Eliminar Utilizador")
        print("4 - Lista de Utilizadores")
        print("5 - Mostrar Artigos de um Utilizador")
        print("6 - Mostrar Interesses de um Utilizador")
        print("7 - Mostrar PyCoins de um Utilizador")
        print("8 - Mostrar Reputação e Comentários de Utilizadores")
        print("V - Voltar Atrás")
        print("S - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("1 - Registo manual ")
            print("2 - Registo por ficheiro")
            op = input()
            if op == "1":
                nome = input("Nome do utilizador: ")
                interesses = input("Interesses (separados por vírgula): ").split(",")
                # Aqui pode-se adicionar uma lógica para adicionar artigos ao utilizador
                artigos_disponiveis = []
                try:
                    feira.registar_utilizador(nome, interesses, artigos_disponiveis)
                    print(f"Utilizador {nome} registrado com sucesso!")
                except Exception as e:
                    print(str(e))
            elif op == "2":
                nome_ficheiro = "utilizadoresartigos.txt"
                avalia_ficheiro = "avaliacoes.txt"
                try:
                    feira.importar_utilizadores(nome_ficheiro)
                    feira.importar_avaliacoes(avalia_ficheiro)
                    print("Registo criado com sucesso.")
                except Exception as e:
                    print(f"Erro ao carregar o ficheiro: {e}")
            else:
                print("Opção inválida. Por favor, tente novamente.")

        elif escolha == "2":  # Alterar Utilizador
            nome = input("Nome do utilizador para alterar: ")
            if nome in feira.utilizadores:
                utilizador = feira.utilizadores[nome]
                
                # Alterar Interesses
                novos_interesses = input("Novos interesses (separados por vírgula): ").split(",")
                utilizador.editar_conta(novos_interesses, utilizador.artigos_disponiveis)

                # Opção para alterar artigos
                alterar_artigos = input("Deseja alterar os artigos existentes? (s/n): ")
                if alterar_artigos.lower() == 's':
                    for artigo in utilizador.artigos_disponiveis:
                        print(f"Alterando {artigo.nome}:")
                        nova_quantidade = int(input("Nova quantidade: "))
                        nova_tipologia = input("Nova tipologia: ")
                        artigo.editar_quantidade(nova_quantidade)
                        artigo.editar_tipo(nova_tipologia)
                        print(f"Artigo '{artigo.nome}' atualizado.")

                # Opção para criar novo artigo
                criar_artigo = input("Deseja criar um novo artigo? (s/n): ")
                if criar_artigo.lower() == 's':
                    nome_artigo = input("Nome do novo artigo: ")
                    preco_artigo = float(input("Preço do artigo: "))
                    tipologia_artigo = input("Tipologia do artigo: ")
                    quantidade_artigo = int(input("Quantidade do artigo: "))
                    novo_artigo = Artigo(nome_artigo, preco_artigo, tipologia_artigo, quantidade_artigo)
                    utilizador.artigos_disponiveis.append(novo_artigo)
                    print(f"Novo artigo '{nome_artigo}' adicionado com sucesso.")

                print(f"Utilizador {nome} alterado com sucesso!")
            else:
                print("Utilizador não encontrado.")


        elif escolha == "3":
            nome = input("Nome do utilizador a eliminar: ")
            try:
                feira.eliminar_conta(nome)
                print(f"Conta de {nome} eliminada com sucesso!")
            except Exception as e:
                print(str(e))

        elif escolha == "4":
            for nome, utilizador in feira.utilizadores.items():
                print(f"Nome: {nome}, Interesses: {', '.join(utilizador.interesses)}, PyCoins: {utilizador.pycoins}")

        elif escolha == "5":
            nome_utilizador = input("Introduza um utilizador para consultar os seus artigos: ")
            if nome_utilizador in feira.utilizadores:
                utilizador = feira.utilizadores[nome_utilizador]
                if utilizador.mostrar_artigos() != "Nenhum artigo disponível.":
                    print(utilizador.mostrar_artigos())
                else:
                    print("Este utilizador não tem artigos.")
            else:
                print("Utilizador não encontrado.")

        elif escolha == "6":
            nome = input("Introduza um nome de utilizador para consultar os seus interesses: ")
            if nome in feira.utilizadores:
                utilizador = feira.utilizadores[nome]
                interesses = utilizador.mostrar_interesses()
                for i, interesse in enumerate(interesses, start=1):
                    print(f"Interesse {i}: {interesse}")
            else:
                print("Utilizador não encontrado.")

        elif escolha == "7":
            nome = input("Introduza um nome de utilizador para consultar os seus Pycoins: ")
            if nome in feira.utilizadores:
                utilizador = feira.utilizadores[nome]
                print(f"Pycoins: {utilizador.pycoins}")
            else:
                print("Utilizador não encontrado.")
                
        elif escolha == "8":
            print("\nListando avaliações de todos os utilizadores:")
            if feira.utilizadores:
                for nome, utilizador in feira.utilizadores.items():
                    utilizador.listar_avaliacoes()
                    print()  # Adiciona uma linha em branco entre as avaliações de cada utilizador
            else:
                print("Não há utilizadores registrados.")
            
        elif escolha.lower() == "v":
            break
        elif escolha.lower() == "s":
            print("Saindo da Feira Virtual. Até logo!")
            break
        else:
            print("Opção inválida.")


def submenu_artigos(feira):
    while True:
        print("\nSubMenu Artigos:")
        print("1 - Mostrar Preço de um Artigo")
        print("2 - Mostrar Quantidade de um Artigo")
        print("3 - Mostrar Tipo de um Artigo")
        print("4 - Editar Nome de um Artigo")
        print("5 - Editar Quantidade de um Artigo")
        print("6 - Editar Tipologia de um Artigo")
        print("7 - Listar Todos os Artigos dos Utilizadores")
        print("8 - Criar um Novo Artigo")
        print("V - Voltar Atrás")
        print("S - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha in ["1", "2", "3", "4", "5", "6"]:
            nome_artigo = input("Introduza o nome do artigo: ")
            artigo_encontrado = False

            for utilizador in feira.utilizadores.values():
                artigo = next((art for art in utilizador.artigos_disponiveis if art.nome == nome_artigo), None)
                
                if artigo:
                    artigo_encontrado = True
                    if escolha == "1":
                        print(f"Preço: {artigo.preco} Pycoins")
                    elif escolha == "2":
                        print(f"Quantidade: {artigo.quantidade}")
                    elif escolha == "3":
                        print(f"Tipologia: {artigo.tipologia}")
                    elif escolha == "4":
                        novo_nome = input("Novo nome do artigo: ")
                        artigo.editar_nome(novo_nome)
                        print(f"Nome do artigo '{nome_artigo}' atualizado para '{novo_nome}'.")
                    elif escolha == "5":
                        nova_quantidade = int(input("Nova quantidade: "))
                        artigo.editar_quantidade(nova_quantidade)
                        print(f"Quantidade do artigo '{nome_artigo}' atualizada para {nova_quantidade}.")
                    elif escolha == "6":
                        nova_tipologia = input("Nova tipologia: ")
                        artigo.editar_tipo(nova_tipologia)
                        print(f"Tipologia do artigo '{nome_artigo}' atualizada para '{nova_tipologia}'.")
                    break

            if not artigo_encontrado:
                print("Artigo não encontrado.")

        elif escolha == "7":
            print("\nListando todos os artigos dos utilizadores:")
            for nome, utilizador in feira.utilizadores.items():
                print(f"\nArtigos do Utilizador {nome}:")
                if utilizador.artigos_disponiveis:
                    for artigo in utilizador.artigos_disponiveis:
                        print(f"- Nome: {artigo.nome}, Preço: {artigo.preco}, Tipologia: {artigo.tipologia}, Quantidade: {artigo.quantidade}")
                else:
                    print("Nenhum artigo disponível.")

        elif escolha == "8":
            nome_utilizador = input("Nome do utilizador para adicionar o artigo: ")
            if nome_utilizador in feira.utilizadores:
                feira.criar_novo_artigo(nome_utilizador)
            else:
                print("Utilizador não encontrado.")

        elif escolha.lower() == "v":
            break
        elif escolha.lower() == "s":
            print("Saindo do submenu Artigos.")
            break
        else:
            print("Opção inválida.")



def submenu_mercado(feira):
    while True:
        print("\nSubMenu Mercado:")
        print("1 - Adicionar Artigo ao Mercado")
        print("2 - Remover Artigo do Mercado")
        print("3 - Listar Artigos do Mercado")
        print("4 - Comprar Artigo ao Mercado")
        print("V - Voltar Atrás")
        print("S - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_utilizador = input("Nome do utilizador (vendedor): ")
            nome_artigo = input("Nome do artigo: ")
            if nome_utilizador in feira.utilizadores:
                preco = float(input("Preço do artigo no Mercado: "))
                quantidade = int(input("Quantidade do artigo a adicionar: "))
                feira.colocar_artigo_para_venda(nome_utilizador, nome_artigo, preco, quantidade)
                print(f"Artigo '{nome_artigo}' adicionado ao Mercado.")
            else:
                print("Utilizador não encontrado.")
            
        elif escolha == "2":
            nome_artigo = input("Nome do artigo a remover do Mercado: ")
            feira.remover_artigo_mercado_utilizadores(nome_artigo)
            print(f"Artigo '{nome_artigo}' removido do Mercado e dos utilizadores.")

        elif escolha == "3":
            print(feira.listar_artigos())
            
        elif escolha == "4":
            artigo_nome = input("Nome do artigo que deseja comprar: ")
           
            feira.listar_vendedores_por_reputacao(artigo_nome)
            vendedor = input("\nEscolha o vendedor pelo nome: ")
            comprador = input("Seu nome de utilizador: ")
            quantidade = int(input("Quantidade a comprar: "))

            try:
                feira.comprar_artigo(comprador, vendedor, artigo_nome, quantidade)
            except Exception as e:
                print(str(e))

        elif escolha.lower() == "v":
            break
        elif escolha.lower() == "s":
            print("Saindo do submenu Mercado.")
            exit()
        else:
            print("Opção inválida.")
            
#Exporta a lista de utilizadores para um ficheiro ordenados por reputação 
def exportar_utilizadores(self, nome_ficheiro):
        with open(nome_ficheiro, "w") as file:
            for nome, utilizador in self.utilizadores.items():
                linha = f"{nome},{','.join(utilizador.interesses)}\n"
                file.write(linha)


def main():
    feira = FeiraVirtual()

    while True:
        print("\nBem-vindo/a à Feira Virtual. Pretende aceder a:")
        print("1 - Utilizadores")
        print("2 - Artigos")
        print("3 - Mercado")
        print("S - Sair")

        escolha_principal = input("Escolha uma opção: ")

        if escolha_principal == "1":
            submenu_utilizadores(feira)
        elif escolha_principal == "2":
            submenu_artigos(feira)
        elif escolha_principal == "3":
            submenu_mercado(feira)
        elif escolha_principal.lower() == "s":
            print("Saindo da Feira Virtual. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()