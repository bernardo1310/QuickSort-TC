# Implementacao do algoritmo QuickSort


def quicksort(lista, nivel=0):
    # Caso base: lista com 0 ou 1 elemento ja esta ordenada
    if len(lista) <= 1:
        return lista

    indent = "   " * nivel

    # O pivo e sempre o primeiro elemento da sublista atual
    pivo = lista[0]

    # Separa os elementos em menores e maiores que o pivo
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    print(f"{indent}Sublista atual: {lista}")
    print(f"{indent}Pivo escolhido: {pivo}")
    print(f"{indent}Menores que {pivo}: {menores}")
    print(f"{indent}Maiores que {pivo}: {maiores}")
    print()

    # Chama o quicksort recursivamente em cada sublista
    if menores:
        print(f"{indent}>>> Sublista esquerda: {menores}")
        esquerda = quicksort(menores, nivel + 1)
    else:
        esquerda = []

    if maiores:
        print(f"{indent}>>> Sublista direita: {maiores}")
        direita = quicksort(maiores, nivel + 1)
    else:
        direita = []

    resultado = esquerda + [pivo] + direita
    print(f"{indent}Combinando: {resultado}")
    print()

    return resultado