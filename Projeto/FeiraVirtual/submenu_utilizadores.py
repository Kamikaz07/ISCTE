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