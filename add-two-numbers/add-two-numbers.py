# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        carry = 0
        current_node = answer
        
        while l1 and l2:
            new_sum = l1.val + l2.val + carry
            new_num = new_sum % 10
            carry = new_sum // 10
            current_node.next = ListNode(val=new_num)
            current_node = current_node.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:  # atleast one node remaining in l1 (loop exited due to l2 == None)
            while l1:
                new_sum = l1.val + carry
                new_num = new_sum % 10
                carry = new_sum // 10
                current_node.next = ListNode(val=new_num)
                current_node = current_node.next
                l1 = l1.next
        elif l2:  # atleast one node remaining in l2 (loop exited due to l1 == None)
            while l2:
                new_sum = l2.val + carry
                new_num = new_sum % 10
                carry = new_sum // 10
                current_node.next = ListNode(val=new_num)
                current_node = current_node.next
                l2 = l2.next
                
        if carry:
            current_node.next = ListNode(val=carry)
            
        return answer.next