class Frutas():
    def __init__(self):
        self.frutas = []
        self.stock = []
        
    def inserir_frutas(self):
        for i in range(6):
            self.frutas.append(input(f"Digite o nome da {i+1}ª fruta: "))
    
    def listar_frutas(self):
        for i in range(len(self.frutas)):
            print(f"{self.frutas[i]}: {self.stock[i]} unidades: ")
    
    def altera_stock(self):
        print("Qual quer alterar?")
        for i, fruta in enumerate(self.frutas):
            print(f"{i + 1}ª - {fruta}: {self.stock[i]}")
        opcao = int(input()) - 1
        quantidade = int(input("Quantas unidades você deseja adicionar ou remover? "))
        if quantidade > 0:
            self.stock[opcao] += quantidade
        elif quantidade < 0:
            if self.stock[opcao] >= abs(quantidade):
                self.stock[opcao] += quantidade
            else:
                print("Quantidade inválida! A quantidade a ser removida é maior do que o estoque disponível.")
        else:
            print("Quantidade inválida! A quantidade precisa ser diferente de zero.")
    
    def inserir_stock(self):
        for i in range(6):
            self.stock.append(int(input(f"Quantos(as) {self.frutas[i]} têm no estoque?\n")))
    
    def excluir_frutas(self,nome):
        for i in range(len(self.frutas)):
            if self.frutas[i] == nome:
                if self.stock[i] == 0:
                    del self.frutas[i]
                    del self.stock[i]
                    break
                else:
                    print("Erro! A fruta não pode ser excluída porque ainda há unidades em estoque.")
                    break
            
def main():
    mercearia = Frutas()
    while True:
        print("\n1. Inserir Frutas")
        print("2. Inserir Stock")
        print("3. Alterar Stock")
        print("4. Excluir Frutas")
        print("5. Listar Frutas")
        print("0. Sair\n")
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            mercearia.inserir_frutas()
        elif opcao == 2:
            mercearia.inserir_stock()
        elif opcao == 3:
            mercearia.altera_stock()
        elif opcao == 5:
            mercearia.listar_frutas()
        elif opcao == 4:
            name = input("Qual fruta quer excluir?")
            mercearia.excluir_frutas(name)
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")
    
if __name__ == "__main__":
    main()