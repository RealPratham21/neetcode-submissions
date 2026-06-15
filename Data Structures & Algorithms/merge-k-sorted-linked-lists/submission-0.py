# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        num_map = defaultdict(int)

        for node in lists:
            curr = node

            while curr:
                num_map[curr.val] += 1

                curr = curr.next

        dummy = ListNode(-1)
        curr = dummy

        for k, v in sorted(num_map.items(), key=lambda x: x[0]):
            for _ in range(v):
                curr.next = ListNode(k)

                curr = curr.next
        
        return dummy.next