class Frutas():
    def __init__(self):
        self.artigos = []
        self.stock = []
        
    def inserir_artigos(self):
        for i in range(6):
            self.artigos.append(input(f"Digite o nome da {i+1}ª fruta: "))
    
    def listar_artigos(self):
        for i in range(len(self.artigos)):
            print(f"{self.artigos[i]}: {self.stock[i]} unidades: ")
    
    def altera_stock(self):
        print("Qual quer alterar?")
        for i, fruta in enumerate(self.artigos):
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
            self.stock.append(int(input(f"Quantos(as) {self.artigos[i]} têm no estoque?\n")))
    
    def excluir_artigos(self,nome):
        for i in range(len(self.artigos)):
            if self.artigos[i] == nome:
                if self.stock[i] == 0:
                    del self.artigos[i]
                    del self.stock[i]
                    break
                else:
                    print("Erro! A fruta não pode ser excluída porque ainda há unidades em estoque.")
                    break