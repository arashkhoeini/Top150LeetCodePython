# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for num in row:
                if num !='.':
                    if num in row_set:
                        return False
                    else:
                        row_set.add(num)
            
        for col_i in range(0,9):
            col_set = set()
            for row_i in range(9):
                num = board[row_i][col_i]
                if num != '.':
                    if num in col_set:
                        return False
                    else:
                        col_set.add(num)
        
        for cell_i in range(0,9):
            cell_set = set()
            for row_i in range((cell_i//3)*3,(cell_i//3)*3+3):
                for col_i in range((cell_i%3)*3,(cell_i%3)*3+3):
                    num = board[row_i][col_i]
                    if num != '.':
                        if num in cell_set:
                            return False
                        else:
                            cell_set.add(num)
        return True