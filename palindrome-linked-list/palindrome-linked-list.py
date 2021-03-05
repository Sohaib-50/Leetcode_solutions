# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Get to middle of linked list
        slow = fast = head
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        
        reversed_second_half = Solution.reverse(slow)
        
        # compare second half to first half
        temp1 = head
        temp2 = reversed_second_half
        while temp2 is not None:
            if temp1.val != temp2.val:
                Solution.reverse(reversed_second_half)
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        
        Solution.reverse(reversed_second_half)
        return True
    
        # temp = head
        # while temp is not None:
        #     print(temp.val, end=" ")
        #     temp = temp.next
    
    def reverse(head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev
    

