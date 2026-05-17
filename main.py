from quicksort import quicksort


def main():
    # Altere esta lista para testar com outros valores
    lista = [5, 1, 4, 3, 2, 6]

    print("=" * 45)
    print("  QUICKSORT - Execucao passo a passo")
    print("=" * 45)
    print(f"\nValores originais: {lista}\n")
    print("-" * 45)
    print()

    lista_ordenada = quicksort(lista)

    print("-" * 45)
    print(f"\nLista ordenada: {lista_ordenada}\n")


if __name__ == "__main__":
    main()