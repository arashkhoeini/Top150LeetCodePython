# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1451890564/?envType=study-plan-v2&envId=top-interview-150

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

from typing import List, Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder.pop(0))
        val_index = inorder.index(root.val)
        left = inorder[:val_index]
        right = inorder[val_index+1:]

        def recursive(node, left, right, order):
            
        
            if len(left) == 0: 
                node.left = None
            elif len(left) == 1:
                node.left = TreeNode(left[0])
                order.pop(order.index(left[0]))
            else:
                node.left = TreeNode(order.pop(0))
                val_index = left.index(node.left.val)
                new_left = left[:val_index]
                new_right = left[val_index+1:]
                recursive(node.left, new_left, new_right, order)
            
            if len(right) == 0: 
                node.right = None
            elif len(right) == 1:
                node.right  = TreeNode(right[0])
                order.pop(order.index(right[0]))
            else:
                node.right = TreeNode(order.pop(0))
                val_index = right.index(node.right.val)
                new_left = right[:val_index]
                new_right = right[val_index+1:]
                recursive(node.right, new_left, new_right, order)

        recursive(root, left, right, preorder)
        return root