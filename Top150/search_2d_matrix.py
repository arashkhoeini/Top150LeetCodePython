# https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find row
        i1 = 0
        i2 = len(matrix)-1
        while i2-i1 > 1:
            mid = (i2+i1)//2
            if target <= matrix[mid][0]:
                i2 = mid
            else:
                i1 = mid
        
        # i1 = i1 if matrix[i2][0] > target else i2

        if matrix[i2][0] <= target:
            i1 = i2
       
        j1,j2 = 0, len(matrix[0])-1
        while j2-j1 > 1:
        
            mid = (j2+j1)//2
            if target == matrix[i1][mid]: return True
            if target < matrix[i1][mid]:
                j2 = mid
            else:
                j1 = mid
            
        return (target == matrix[i1][j1]) or (target == matrix[i1][j2])
