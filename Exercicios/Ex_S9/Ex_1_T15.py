'''
#1
class ID:
    def __init__(self):
        self.nums = ["id","id","id","id","id","id","id","id","id","id"]

     
#2
# Cria a lista
lista = [0] * 100

# Preenche cada posição com o seu número
for i in range(100):
    lista[i] = i

# Imprime o valor contido em todas as posições, uma por linha
for num in lista:
    print(num)
    
#3
lista = [""] * 50
for i in range(50):
    lista[i] = "id " + str(i)
    print(lista)

#4
import random 
lista = ["Bruno"], ["Ines"], ["Sara"], ["Miguel"]
a = random.randint(0, len(lista))
print(lista[a])
'''

