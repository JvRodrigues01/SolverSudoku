import time
import timeit

# N é o tamanho da matriz 2D N*N
N = 9
 
# Uma função helper para printar a grid
def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
# Verifica se será válido atribuir valor a coluna
def isSafe(grid, row, col, num):
   
    for x in range(9):
        if grid[row][x] == num:
            return False
 
    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

# Pega uma grid parcialmente preenchida e tenta
# atribuir valores a todos os locais não atribuídos, ou seja que estão com 0
def solveSudoku(grid, row, col):
    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0
 
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):
       
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0

    return False
 
# Grid padrão
 
# 0 significa células não atribuídas
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
if (solveSudoku(grid, 0, 0)):
    start = timeit.default_timer()

    printing(grid)

    stop = timeit.default_timer()
    time = stop-start
    print("Tempo de execução: ",format(time, '.8f'))
    
else:
    print("Não Existe Solução")