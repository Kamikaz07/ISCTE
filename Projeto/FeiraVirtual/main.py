#Rodrigo Fonseca 111713
#Sara Pereira 123562

# Importação das classes e funções necessárias dos outros ficheiros
from feira_virtual import FeiraVirtual
from submenu_utilizadores import submenu_utilizadores
from submenu_artigos import submenu_artigos
from submenu_mercado import submenu_mercado

# Função principal que executa o programa
def main():
    # Cria uma instância da Feira Virtual
    feira = FeiraVirtual()

    # Loop infinito para manter o programa em execução até que o usuário decida sair
    while True:
        # Apresenta as opções disponíveis para o usuário
        print("\nBem-vindo/a à Feira Virtual. Pretende aceder a:")
        print("1 - Utilizadores")
        print("2 - Artigos")
        print("3 - Mercado")
        print("S - Sair")

        # Solicita a escolha do usuário
        escolha_principal = input("Escolha uma opção: ")

        # Direciona para o submenu adequado com base na escolha do utilizador
        if escolha_principal == "1":
            submenu_utilizadores(feira)
        elif escolha_principal == "2":
            submenu_artigos(feira)
        elif escolha_principal == "3":
            submenu_mercado(feira)
        elif escolha_principal.lower() == "s":
            # Sai do programa
            print("Saindo da Feira Virtual. Até logo!")
            break
        else:
            # Mensagem de erro para escolha inválida
            print("Opção inválida. Por favor, tente novamente.")

# Garante que o script só executa a função main se for o script principal executado
if __name__ == "__main__":
    main()
