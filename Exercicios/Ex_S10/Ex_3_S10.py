def preencher_matriz():
    matriz = [' '] * 9
    jogadores = ['X', 'O']
    jogador_atual = 0

    for i in range(9):
        print(f"Jogador {jogadores[jogador_atual]}, é a sua vez.")
        posicao = int(input("Digite a posição (0-8): "))

        while not (0 <= posicao < 9) or matriz[posicao] != ' ':
            print("Posição inválida. Tente novamente.")
            posicao = int(input("Digite a posição (0-8): "))
        matriz[posicao] = jogadores[jogador_atual]
        jogador_atual = 1 - jogador_atual 

        exibir_jogo(matriz)

    return matriz


def exibir_jogo(matriz):
    print('-------------')
    print(f'| {matriz[0]} | {matriz[1]} | {matriz[2]} |')
    print('-------------')
    print(f'| {matriz[3]} | {matriz[4]} | {matriz[5]} |')
    print('-------------')
    print(f'| {matriz[6]} | {matriz[7]} | {matriz[8]} |')
    print('-------------')


def verificar_vencedor(matriz):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]

    for combinacao in combinacoes_vencedoras:
        a, b, c = combinacao
        if matriz[a] == matriz[b] == matriz[c] != ' ':
            return matriz[a] 
    return None  


def verificar_empate(matriz):
    return ' ' not in matriz


def main():
    matriz = preencher_matriz()
    vencedor = verificar_vencedor(matriz)

    if vencedor:
        print(f"Jogador {vencedor} venceu!")
    else:
        if verificar_empate(matriz):
            print("Empate!")
        else:
            print("O jogo não foi concluído.")
    print("Fim do jogo.")


if __name__ == "__main__":
    main()