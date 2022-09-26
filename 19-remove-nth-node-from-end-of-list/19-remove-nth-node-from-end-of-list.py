# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return head.next
        
        dummy = ListNode()
        dummy.next = head
        current = dummy

        while True:  # change condition
            temp = current
            
            # check if next node is nth node from last
            # by moving n steps ahead and then seeing if its last node
            for i in range(n):
                temp = temp.next
            if not temp.next:
                current.next = current.next.next
                break
            
            current = current.next
        
        return dummy.next