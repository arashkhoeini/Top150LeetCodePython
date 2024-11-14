# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


from typing import List, Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def recursive(node, right, left, order):
            # print(root)
            if len(right) == 0:
                node.right = None
            elif len(right) == 1:
                node.right = TreeNode(right[0])
                order.remove(right[0])
            else:
                node.right = TreeNode(order[-1])
                val_index = right.index(node.right.val)
                new_right = right[val_index+1:]
                new_left = right[:val_index]
                order.remove(node.right.val)
                recursive(node.right, new_right, new_left, order)
            # print(root)
            if len(left) == 0:
                node.left = None
            elif len(left) == 1:
                node.left = TreeNode(left[0])
                order.remove(left[0])
            else:
                node.left = TreeNode(order[-1])
                val_index = left.index(node.left.val)
                new_left = left[:val_index]
                new_right = left[val_index+1:]
                order.remove(node.left.val)
                recursive(node.left, new_right, new_left, order)
            
        root = TreeNode(postorder[-1])
        val_index = inorder.index(postorder[-1])
        right = inorder[val_index+1:]
        left = inorder[:val_index]
        postorder.pop(-1)
            
        recursive(root, right, left, postorder)
        return root 