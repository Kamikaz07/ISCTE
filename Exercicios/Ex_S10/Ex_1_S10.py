import random

def maior(temperatura):
    max_temp_L = temperatura[0][0]
    max_temp_P = temperatura[0][1]
    max_temp_F = temperatura[0][2]
    max_temp_C = temperatura[0][3]
    max_temp_A = temperatura[0][4]
    for i in range(5): # Corrigido
        for j in range(1, 4): # Corrigido
            if temperatura[i][j] > max_temp_L: # Corrigido
                max_temp_L = temperatura[i][j]
            if temperatura[i][j] > max_temp_P: # Corrigido
                max_temp_P = temperatura[i][j]
            if temperatura[i][j] > max_temp_F: # Corrigido
                max_temp_F = temperatura[i][j]
            if temperatura[i][j] > max_temp_C: # Corrigido
                max_temp_C = temperatura[i][j]
            if temperatura[i][j] > max_temp_A: # Corrigido
                max_temp_A = temperatura[i][j]
            
    return max_temp_L, max_temp_P, max_temp_F, max_temp_C, max_temp_A

def menor(temperatura):
    min_temp_L = temperatura[0][0]
    min_temp_P = temperatura[0][1]
    min_temp_F = temperatura[0][2]
    min_temp_C = temperatura[0][3]
    min_temp_A = temperatura[0][4]
    
    for i in range(1, len(temperatura)):
        for j in range(5):
            if temperatura[i][j] < min_temp_L:
                min_temp_L = temperatura[i][j]
            if temperatura[i][j] < min_temp_P:
                min_temp_P = temperatura[i][j]
            if temperatura[i][j] < min_temp_F:
                min_temp_F = temperatura[i][j]
            if temperatura[i][j] < min_temp_C:
                min_temp_C = temperatura[i][j]
            if temperatura[i][j] < min_temp_A:
                min_temp_A = temperatura[i][j]
                
    return min_temp_L, min_temp_P, min_temp_F, min_temp_C, min_temp_A


def dados():
    temperatura = [[random.randint(0, 100), 
                    random.randint(0, 100), 
                    random.randint(0, 100), 
                    random.randint(0, 100), 
                    random.randint(0, 100)] 
                   for _ in range(5)]
    return temperatura # Retorna a lista temperatura
        
def main():
    temp = dados()
    maior_temp = maior(temp)
    menor_temp = menor(temp)
    print("Maior temperatura:", maior_temp)
    print("Menor Temperatura:", menor_temp)

if __name__ == "__main__":
    main()