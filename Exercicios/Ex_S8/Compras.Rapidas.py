def escolher_caixa(nr_art):
    if(nr_art >= 5):
        return "normal"
    return "rápida"

def main():
    n_art = int(input("Numero de Artigos:\n"))
    caixa = escolher_caixa(n_art)
    print ("Deve dirigir-se à caixa: " + str(caixa))
    

if __name__ == "__main__":
    main()
    