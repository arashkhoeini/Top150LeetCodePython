# https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150

# Given the head of a linked list, rotate the list to the right by k places.

from . import ListNode
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # n is size of the list
        # set the next node of n-k to None
        # move the head to n-k+1
        # set the next node of nth node to the original head

        dummy = head 
        n = 0
        while dummy:
            dummy = dummy.next
            n += 1
        if n==0: return None
        if k%n==0: return head
        if (k==0) or (k==n): return head
        
        current_head = head
        i = 1
        new_head = None
        while current_head.next:
            if i == (n-(k%n)):
                temp = current_head
                current_head = current_head.next
                new_head = current_head
                temp.next = None
            else:
                current_head = current_head.next
            i += 1
        current_head.next = head

        return new_head #if new_head is not None else head
