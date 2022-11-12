# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_lst = 0
        current = head
        while current:
            len_lst += 1
            current = current.next
            
        dummy = ListNode()
        dummy.next = head
        current = dummy
        for i in range(len_lst - n):
            current = current.next
            
        current.next = current.next.next
        
        return dummy.next
            