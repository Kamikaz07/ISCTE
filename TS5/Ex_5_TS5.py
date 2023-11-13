
def criar_desenho(largura):
    for linha in range(largura):
        for coluna in range(largura):
            if (linha + coluna) % 2 == 0:
                print("^", end="")
            else:
                print("*", end="")
        print()

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    criar_desenho(numero)


if __name__ == "__main__":
    main()