
#1
    # Pede ao utilizador para inserir as notas
primeiro_teste = input()
segundo_teste = input()
projeto = input()

    # Valida os dados para ver se estão nos parametros certos
try:
    primeiro_teste = float(primeiro_teste)
    segundo_teste = float(segundo_teste)
    projeto = float(projeto)
    if primeiro_teste < 0 or primeiro_teste > 20 or segundo_teste < 0 or segundo_teste > 20 or projeto < 0 or projeto > 20:
        raise ValueError
except ValueError:
    print("Número inválido.")
    exit()
    
    #Calcula a nota final
nota_final = 0.25 * primeiro_teste + 0.25 * segundo_teste + 0.5 * projeto
print(nota_final)


#2.
    # Recebe os 4 números do utilizador
num1 = input()
num2 = input()
num3 = input()
num4 = input()

    # Valida os dados para ver se estão nos parametros certos
try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
except ValueError:
    print("Número inválido.")
    exit()
    
numeros = [num1, num2, num3, num4]
    # Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

    # Exibe os números em ordem decrescente
print(end="")
for numero in numeros:
    print(numero, end=" ")


#3
def calcular_custo_total(estrada):
    # Verifica a designação da estrada e obter os custos correspondentes
    if estrada == "A1":
        custo_km = 0.3
        custo_portagens = 7
    elif estrada == "A20":
        custo_km = 0.4
        custo_portagens = 15
    elif estrada == "A21":
        custo_km = 0.15
        custo_portagens = 5.75
    else:
        return "Estrada não encontrada."
    
    # Calcula o custo total da alternativa
    distancia = 120
    custo_combustivel = custo_km * distancia
    custo_total = custo_combustivel + custo_portagens
    return custo_total

    # Solicita ao utilizador a designação da estrada
estrada = input("Digite a designação da estrada (A1, A20 ou A21): ")

    # Calcula o custo total da alternativa
custo_total = calcular_custo_total(estrada)

    # Exibe o custo total da alternativa
print(custo_total)


#4
def calcular_vencimento_liquido(vencimento_bruto):
        # Calcula os descontos
    desconto_irs = 0.25 * vencimento_bruto
    desconto_seg_social = 0.05 * vencimento_bruto
    desconto_caixa_aposentacoes = 0.1 * vencimento_bruto

        # Calcula o vencimento líquido
    vencimento_liquido = vencimento_bruto - desconto_irs - desconto_seg_social - desconto_caixa_aposentacoes
    return vencimento_liquido

    # Solicita ao utilizador o vencimento bruto
vencimento_bruto = input()

    # Valida os dados para ver se estão nos parametros certos
try:
    vencimento_bruto = float(vencimento_bruto)
except ValueError:
    print("Vencimento bruto inválido.")
    exit()
    
    # Calcula o vencimento líquido
vencimento_liquido = calcular_vencimento_liquido(vencimento_bruto)

    # Exibe o vencimento líquido
print(vencimento_liquido)


#5
    # Solicita ao utilizador um número entre 1 e 12
numero = input("Digite um número entre 1 e 12: ")

    # Valida os dados para ver se estão nos parametros certos
try:
    numero = int(numero)
    if numero < 1 or numero > 12:
        raise ValueError
except ValueError:
    print("Número inválido.")
    exit()
    
    # Cria uma lista com os nomes dos meses
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    # Obtêm o mês correspondente
mes = meses[numero - 1]

    # Exibe o mês correspondente
print(mes)
