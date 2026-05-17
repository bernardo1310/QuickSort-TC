# QuickSort em Python

Implementação didática do algoritmo de ordenação QuickSort feita do zero em Python, sem utilizar nenhuma função pronta de ordenação como `sort()` ou `sorted()`.

## O que o projeto faz

Você informa uma lista de números, o programa exibe os valores originais e mostra passo a passo como o QuickSort vai dividindo e ordenando a lista, até chegar ao resultado final.

## Estrutura do projeto

```
quicksort/
├── main.py        # Ponto de entrada: define a lista e exibe a execução
└── quicksort.py   # Lógica do algoritmo QuickSort
```

## Como executar

1. Certifique-se de ter o **Python 3** instalado
2. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
3. Entre na pasta e execute:
   ```bash
   python main.py
   ```

## Como testar com outros valores

Abra o arquivo `main.py` e altere a linha:

```python
lista = [5, 1, 4, 3, 2, 6]
```

Substitua pelos números que quiser e rode novamente.

## Exemplo de saída

```
Valores originais: [5, 1, 4, 3, 2, 6]

Sublista atual: [5, 1, 4, 3, 2, 6]
Pivo escolhido: 5
Menores que 5: [1, 4, 3, 2]
Maiores que 5: [6]

>>> Sublista esquerda: [1, 4, 3, 2]
   Pivo escolhido: 1
   ...

Lista ordenada: [1, 2, 3, 4, 5, 6]
```

## Tecnologias

- Python 3
- Sem bibliotecas externas
