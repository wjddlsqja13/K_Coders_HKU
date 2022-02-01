# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Runtime에서 LL을 따라갈수는 없지만, LL개념이 헷갈린다면 기본적인 list를 사용해서도 풀이 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        nodes = []
        duplicate = []
        #duplicate = dict()
        if node is None:
            return
        
        while node.next != None:                    
            if node.val == node.next.val:
                duplicate.append(node.val)
            nodes.append(node.val)    
            node = node.next
            
        nodes.append(node.val)
        
        result = []
        
        for i in nodes:
            if i not in duplicate:
                result.append(i)
                
        ans = dummy = ListNode()
        
        for a in result:
            ans.next = ListNode(a)
            ans = ans.next
            
        return dummy.next
        

