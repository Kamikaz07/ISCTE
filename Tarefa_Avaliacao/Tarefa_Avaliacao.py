def valida_numero_utilizador(num_utilizador):
    if num_utilizador < 10:
        return False
    else:
        return True

def mostra_multiplos(num_utilizador):
    print(end="")
    for i in range(10, num_utilizador):
        if i % 3 == 0:
            print(i, end=" ")   

def main():
    num_utilizador = int(input())
    valido = valida_numero_utilizador(num_utilizador)
    
    if not valido:
        print("Número inválido")
    mostra_multiplos(num_utilizador)
    

if __name__ == "__main__":
    main()