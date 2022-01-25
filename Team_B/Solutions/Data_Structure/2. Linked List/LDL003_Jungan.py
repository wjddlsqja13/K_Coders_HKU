# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(None)
        dummy.next = head
        
        while head != None and head.next != None:
            if head.val == head.next.val :
                #2번 이상 반복되는 경우
                while head.next != None and head.val == head.next.val :
                    head = head.next
                curr.next = head.next
            else :
                curr = curr.next
            head = head.next
        
        return dummy.next