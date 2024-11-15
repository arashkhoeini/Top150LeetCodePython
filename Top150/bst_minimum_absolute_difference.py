# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

from typing import Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.sorted_values = []
        def inorder(node):
            if node.left: inorder(node.left)
            self.sorted_values.append(node.val)
            if node.right: inorder(node.right)
        inorder(root)
        diff = float('inf')
        for i in range(len(self.sorted_values)-1):
            if (self.sorted_values[i+1] - self.sorted_values[i]) < diff:
                diff = self.sorted_values[i+1] - self.sorted_values[i]
        return diff