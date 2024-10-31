# Leitura da entrada e conversão para uma lista de inteiros
copos = list(map(int, input().split()))

# Identifica o índice do copo com o valor 1 e soma 1 para ajustar a posição
posicao_feijao = copos.index(1) + 1

# Imprime a posição do copo onde está o feijão
print(posicao_feijao)
