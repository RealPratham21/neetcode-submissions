# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_len = 0

        curr = head

        while curr:
            total_len += 1
            curr = curr.next
        
        dummy = ListNode(-1, head)

        curr = dummy
        cpos = 0

        while cpos != (total_len - n):
            curr = curr.next
            cpos += 1
        
        curr.next = curr.next.next

        return dummy.next