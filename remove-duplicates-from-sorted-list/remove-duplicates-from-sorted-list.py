# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:  # if empty or 1-element list
            return head
        
        temp = head
        while temp.next is not None:
            if temp.next.val == temp.val:
                temp.next = temp.next.next  # remove the very next pointer from the list
            else:
                temp = temp.next  # move temp pointer ahead
                
        return head