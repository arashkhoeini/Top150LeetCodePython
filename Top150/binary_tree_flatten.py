# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150

# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# This is actually not my own solution. My solution (the commented out solution) was working fin but it was using O(n) space.
# This solution is using O(1) space. 

from typing import Optional
from .binary_tree_max_depth import TreeNode

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if root is None: return
        # if (root.left is None) and (root.right is None): return 
        # node_list = []
        # if root.right: node_list.append(root.right)
        # if root.left: node_list.append(root.left)
        # parent = root
        # while len(node_list) > 0:
        #     node = node_list.pop(-1)
        #     if node.right: node_list.append(node.right)
        #     if node.left: node_list.append(node.left)

        #     parent.left = node
        #     parent = node
        # # print(root)
        # node = root
        # while node.left:
        #     node.right = node.left
        #     node.left = None
        #     node = node.right

        curr = root
        
        while curr:
            if curr.left != None:
                p = curr.left
                while p.right != None:
                    p = p.right
                    
                p.right = curr.right
                
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right