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