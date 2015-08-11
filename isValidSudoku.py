__author__ = 'cenk'

# @param {character[][]} board
# @return {boolean}
def isValidSudoku(board):

    colSet = set()
    for i in range(9):
        colSet.clear()
        for k in range(9):
            if board[k][i] != '.':
                if board[k][i] in colSet:
                    return False
                else:
                    colSet.add(board[k][i])

    rowSet = set()
    for i in range(9):
        rowSet.clear()
        for k in range(9):
            if board[i][k] != '.':
                if board[i][k] in rowSet:
                    return False
                else:
                    rowSet.add(board[i][k])

    boxSet = set()
    for i in range(0,9,3):
        for k in range(0,9,3):
            boxSet.clear()
            for j in range(i,i+3):
                for l in range(k,k+3):
                    print j,l
                    if board[j][l] != '.':
                        if board[j][l] in boxSet:
                            return False
                        else:
                            boxSet.add(board[j][l])

    return True





b = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
board = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','1','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']
         ]

print isValidSudoku(b)