def main():
    numero = int(input("Insira um número: "))

    if numero < 10:
        print("Valor inválido.")
    else:
        for i in range(10, numero + 1):
            if i % 3 == 0:
                print(i)

if __name__ == "__main__":
    main() 

