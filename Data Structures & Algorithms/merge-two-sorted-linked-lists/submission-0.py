# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        c1 = list1

        while c1:
            vals.append(c1.val)
            c1 = c1.next

        c2 = list2

        while c2:
            vals.append(c2.val)
            c2 = c2.next

        vals.sort()

        res = ListNode(-1)

        curr = res

        for i in vals:
            curr.next = ListNode(i)
            curr = curr.next
        
        return res.next