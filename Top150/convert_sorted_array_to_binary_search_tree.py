# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums where the elements are sorted in ascending order, convert it to a  height-balanced  binary search tree.

from typing import List, Optional
from .binary_tree_max_depth import TreeNode
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.recursive(nums)
    
    def recursive(self, nums):
        if len(nums) == 0: return None
        if len(nums) == 1: return TreeNode(val=nums[0])
        
        middle = len(nums) // 2
        root = TreeNode(val=nums[middle])
        
        root.left = self.recursive(nums[:middle])
        root.right = self.recursive(nums[middle+1:])

        return root