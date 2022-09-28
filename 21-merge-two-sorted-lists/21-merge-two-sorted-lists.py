# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2:
                return None
            return list2
        elif not list2:
            return list1
        
        current1 = list1
        current2 = list2
        answer_dummy_head = ListNode()
        if list1.val < list2.val:
            answer_dummy_head.next = list1
            current1 = current1.next
        else:
            answer_dummy_head.next = list2
            current2 = current2.next
        
        current = answer_dummy_head.next
        while current1 or current2:
            if not current1:
                current.next = current2
                current2 = None
            elif not current2:
                current.next = current1
                current1 = None
            elif current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next
                
        return answer_dummy_head.next
                
                
                
            