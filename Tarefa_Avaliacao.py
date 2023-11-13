def conta_pares(num_utilizador):
    qnt = 0
    for i in range(num_utilizador):
        if i % 2 == 0:
            qnt = qnt + 1
    return qnt        

def main():
    num_utilizador = int(input())
    qnt_pares = conta_pares(num_utilizador)
    print(qnt_pares)

if __name__ == "__main__":
    main()


