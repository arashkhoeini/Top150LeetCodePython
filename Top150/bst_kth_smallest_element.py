# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

from typing import Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = 0
        self.val = None
        def inorder(node):
            if self.kth < k:
                if node.left:  inorder(node.left)
                self.kth += 1
                if self.kth == k: 
                    self.val = node.val 
                    return
                if node.right:  inorder(node.right)
            else: return 
        inorder(root)
        return self.val