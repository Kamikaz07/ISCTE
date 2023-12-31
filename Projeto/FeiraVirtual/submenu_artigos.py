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