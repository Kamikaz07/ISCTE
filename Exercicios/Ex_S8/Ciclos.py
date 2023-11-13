def main():
    res = 0
    parar = ''
    while parar != 'n':
        num = int(input("Introduza um valor a somar\n"))
        res = num + res
        print(res)
        parar = input("Deseja continuar a somar números? s/n: ")



if __name__ == "__main__":
    main()