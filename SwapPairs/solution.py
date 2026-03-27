# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head:
            return None
        else:
            second_head = head.next
            current = head

            while current and current.next:
                first = current
                second = current.next

                first.next = second.next
                second.next = first
                if prev:
                    prev.next = second
                prev = first
                current = first.next

        return head