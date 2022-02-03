# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 뭔가 너무 생각나는대로 구현한 코드, 가독성을 높이기위해 불필요한 것들을 제거할 필요가있다... 
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count_node = head
        count = 0
        
        while (count_node):
            count += 1
            count_node = count_node.next
            
        current = head
        dummy = ListNode(None)
        start = head
        cycle = 0
        
        while count >= k:
            prev = None
            if cycle > 0:
                temp = current
            for i in range(k):                
                next = current.next
                current.next = prev
                prev = current
                current = next
            if cycle == 0:
                dummy.next = prev
            if cycle >0:
                
                start.next = prev
                start = temp
                start.next = current
            cycle += 1
            count -= k
        start.next = current
        return dummy.next
                
