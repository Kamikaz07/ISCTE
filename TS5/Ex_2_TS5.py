class NotasSemestre:
    def __init__(self):
        self.notas = [0, 0, 0, 0, 0]  # Lista para armazenar as notas das UCs


    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def mostrar_notas(self):
        for i, nota in enumerate(self.notas):
            print(f"Nota da UC {i+1}: {nota}")
    
    def alterar_nota(self, uc, nota):
        if uc >= 1 and uc <= 5:
            self.notas[uc-1] = nota
        else:
            print("UC inválida!")
    
    def main(self):
        notas_semestre = NotasSemestre()

        for i in range(5):
            nota = float(input(f"Insira a nota final da UC {i+1}: "))
            notas_semestre.alterar_nota(i+1, nota)

        uc_escolhida = int(input("Escolha o número da UC para ver a nota final: "))
        notas_semestre.mostrar_notas()
        print(f"Nota final da UC {uc_escolhida}: {notas_semestre.notas[uc_escolhida-1]}")
        print(f"Média total: {notas_semestre.calcular_media()}")
        


notas_semestre = NotasSemestre()
notas_semestre.main()
      
    