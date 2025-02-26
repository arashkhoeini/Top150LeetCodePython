# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        size = 0
        while dummy:
            size += 1
            dummy = dummy.next
        
        # if n == size: return None

        target = size - n
        print(size, target)
        if target+1 == 1: 
            head = head.next
            return head

        counter = 1
        temp_head = head
        while counter != target:
            counter += 1
            temp_head = temp_head.next
        
        temp_head.next = temp_head.next.next

        return head
