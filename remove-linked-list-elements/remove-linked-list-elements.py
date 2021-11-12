# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        current = head
        
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
            
            
        return dummy_head.next