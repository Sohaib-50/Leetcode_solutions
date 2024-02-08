# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head

        behind = dummy_head
        ahead = dummy_head

        # give head start
        for _ in range(n):
            ahead = ahead.next

        while ahead.next is not None:
            ahead = ahead.next
            behind = behind.next
        
        # remove
        behind.next = behind.next.next

        return dummy_head.next
