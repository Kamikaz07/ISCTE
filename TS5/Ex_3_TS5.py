def main():
    num = 0
    maior = 0
    for i in range(10):
        num = int(input(f"Digite o {i+1} número\n"))
        if(num > maior):
            maior = num
    print("Maior Número - ", maior) 
        
if __name__ == "__main__":
    main()