class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counter = 0

        for i, row in enumerate(board):
            for j, cell in enumerate(row):

                if i == 9 or j == 9:
                    continue

                for cell2 in row[j+1:len(row)]:
                    counter+=1
                    if (not validCells(cell, cell2)):
                        return False
                
                for k in range(1, 9-i):
                    counter+=1
                    cell2 = board[i+k][j]
                    if (not validCells(cell, cell2)):
                        return False

                row_end = (i//3)*3+3
                col_end = (j//3)*3+3
                for k in range(i, row_end):
                    for l in range(j, col_end):
                        counter+=1
                        if (k==i and l==j):
                            continue

                        cell2 = board[k][l]
                        if (not validCells(cell, cell2)):
                            return False

        return True

def validCells(c1: str, c2: str) -> bool:
    return c1 == '.' or c1 != c2