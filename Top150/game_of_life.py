# https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        scores = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                neighbors = [(i-1, j-1), (i-1,j), (i-1, j+1), (i,j-1), (i,j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                neighbors = [(i,j) for i,j in neighbors if ((0<=i<=m-1) and (0<=j<=n-1))]
                scores[i][j] = sum([board[i][j] for i,j in neighbors])
                

        for i in range(m):
            for j in range(n):
                if scores[i][j] < 2:
                    board[i][j] = 0
                elif scores[i][j] > 3:
                    board[i][j] = 0
                else:
                    if board[i][j] == 1:
                        board[i][j] = 1
                    elif scores[i][j] == 3:
                        board[i][j] = 1
