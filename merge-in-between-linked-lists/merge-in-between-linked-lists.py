# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # headforlist2
        
        i = 0
        temp = list1
        while i < a - 1:
            temp = temp.next
            i += 1
            
        headforlist2 = temp
        
        while i <= b:
            temp = temp.next
            i += 1
            
        tailforlist2 = temp
        
        # lastnodeoflist2
        lastnodeoflist2 = list2
        next_node = list2.next
        while next_node:
            lastnodeoflist2 = lastnodeoflist2.next
            next_node = next_node.next
            
        headforlist2.next = list2
        lastnodeoflist2.next = tailforlist2
        
        return list1