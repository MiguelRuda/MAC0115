import sys

def criaMatriz(nome):
    try:
        arquivo = open(nome, 'r')
    except IOError:
        print('Não consegui abrir o arquivo', arquivo)
        sys.exit(0)
    
    matriz = []
    for linha in arquivo:
        linha_matriz = linha.split()
        matriz.append(linha_matriz)
    arquivo.close()
    return matriz

# função auxiliar para verificar se todos os elementos de uma lista possuem valor zero
def soZeros(lista):
    zeros = True
    for i in lista:
        if int(i) != 0:
            zeros = False
    return zeros

# Programa Principal

# lê o nome do arquivo como argumento e cria a matriz
nome_arquivo = sys.argv[1]
matriz = criaMatriz(nome_arquivo)

# calcula a ordem da matriz quadrada
tam = len(matriz)

# verifica se tem alguma LINHA da matriz formada só por zeros
linha_zeros = False
i = 0
while not(linha_zeros) and i < tam:
    linha_zeros = soZeros(matriz[i])
    i = i + 1

if linha_zeros:
    print('Matriz possui linhas nulas')
else:
    print('Matriz NÃO possui linhas nulas')

# verifica se tem alguma COLUNA da matriz é formada só por zeros
coluna_zeros = False
j = 0
while not(coluna_zeros) and j < tam:
    coluna_matriz = []
    for i in range(tam): # constrói uma lista da coluna j da matriz
        coluna_matriz.append(matriz[i][j])
    coluna_zeros = soZeros(coluna_matriz)
    j = j + 1

if coluna_zeros:
    print('Matriz possui colunas nulas')
else:
    print('Matriz NAO possui colunas nulas')

# verifica se a DIAGONAL PRINCIPAL da matriz é formada só por zeros
diagonal = []
for i in range(tam): # constrói uma lista com a diagonal principal da matriz
    diagonal.append(matriz[i][i])

if soZeros(diagonal):
    print('Matriz possui diagonal principal nula')
else:
    print('Matriz NAO possui diagonal principal nula')
