# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # get slow pointer to middle of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        current = slow
        prev = None
        while current != fast:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        max_sum = float('-inf')
        max_sum =  0
        left = head
        right = prev
        while right:
            max_sum = max(max_sum, left.val + right.val)
            right = right.next
            left = left.next

        return max_sum
            

        
