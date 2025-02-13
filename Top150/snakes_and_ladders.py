from typing import List
from math import ceil

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.board = board
       
        q = [1]
        visited = {1:0}
        n = len(board)
        while q:
            current = q.pop(0)
            n_dice = visited[current]
            for i in range(current+1, min(current+6, n*n)+1):
                dest = self.itoi(i, n)
                if dest in visited:
                    visited[dest] = min(visited[dest], n_dice+1)
                else:
                    q.append(dest)
                    visited[dest] = n_dice+1
        
        if n*n in visited: return visited[n*n]
        return -1
    
    def itoloc(self,i,n):
        row = n-ceil(i/n)
        col = (i-1)%n
        if (n-row)%2 == 1:
            return (row,col)
        else:
            return (row, n-1-col)

    def itoi(self,i,n):
        row, col = self.itoloc(i,n)
        if self.board[row][col] == -1:
            dest = i
        else:
            dest =  self.board[row][col]
        return dest