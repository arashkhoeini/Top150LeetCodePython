# https://leetcode.com/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from typing import Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.sorted_nodes = []
        def inorder(node):
            if node.left: inorder(node.left)
            self.sorted_nodes.append(node.val)
            if node.right: inorder(node.right)
        
        inorder(root)
        if len(set(self.sorted_nodes)) < len(self.sorted_nodes):
            return False
        return self.sorted_nodes == sorted(self.sorted_nodes)