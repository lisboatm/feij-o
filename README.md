# Adivinhe Onde o Feijão Está

## Descrição

Esse problema envolve identificar em qual copo se encontra um feijão após uma partida de adivinhação. São dados quatro copos, e exatamente um deles possui o feijão no final do jogo. Nosso objetivo é determinar o número do copo onde o feijão está localizado.

## Entrada

A entrada consiste em uma linha com quatro inteiros, `C1, C2, C3, C4`, onde:
- `Ci = 1` indica que o feijão está no copo `i`.
- `Ci = 0` indica que o copo `i` está vazio.

A entrada sempre terá exatamente um valor `1` e três valores `0`.

### Exemplo

```plaintext
0 0 0 1
```

## Saída

A saída deve ser um único número inteiro entre 1 e 4, que indica a posição do copo onde o feijão está.

### Exemplo de Saída

Para a entrada acima, a saída seria:

```plaintext
4
```

## Exemplos

| Entrada     | Saída |
|-------------|-------|
| `0 1 0 0`   | 2     |
| `1 0 0 0`   | 1     |
| `0 0 1 0`   | 3     |
| `0 0 0 1`   | 4     |

## Solução

Para resolver o problema, podemos seguir os seguintes passos:

1. **Ler a linha de entrada** e transformá-la em uma lista de inteiros.
2. **Identificar a posição do número 1** na lista, que representa o copo onde o feijão está.
3. Ajustar a posição encontrada (como o índice começa em 0, somamos 1 para ajustar de acordo com a numeração dos copos de 1 a 4).
4. **Imprimir a posição** resultante.

### Código em Python

```python
# Leitura da entrada e conversão para uma lista de inteiros
copos = list(map(int, input().split()))

# Identifica o índice do copo com o valor 1 e soma 1 para ajustar a posição
posicao_feijao = copos.index(1) + 1

# Imprime a posição do copo onde está o feijão
print(posicao_feijao)
```

### Explicação do Código

- **`map(int, input().split())`** converte a linha de entrada em uma lista de inteiros.
- **`copos.index(1)`** encontra o índice onde o feijão está (onde o valor é `1`).
- **`+ 1`** ajusta o índice para retornar a numeração do copo no intervalo de 1 a 4.

## Complexidade

Essa solução é **O(1)** em tempo, pois a lista sempre possui quatro elementos, e a busca do índice é constante.
