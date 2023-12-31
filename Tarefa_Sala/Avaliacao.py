import random

def criar_matriz_vazia():
    matriz = [[random.randint(0, 99) for _ in range(4)] for _ in range(4)]
    return matriz

def contar_vizinhos_menores(matriz):
    contador = 0
    for i in range(4):
        for j in range(4):
            if j > 0 and matriz[i][j] > matriz[i][j-1]:
                contador += 1
    return contador

def main():
    matriz = criar_matriz_vazia()
    contador = contar_vizinhos_menores(matriz)
    print(matriz)
    print(contador)

if __name__ == "__main__":
    main()