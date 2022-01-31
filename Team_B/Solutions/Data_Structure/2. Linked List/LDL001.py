class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        result = []        
        for l in lists:
            node = l
            while node:
                result.append(node)
                node = node.next
            
        if lists == None or result == []:
            return None
                
        result.sort(key = lambda x: x.val)       
        
        for i in range(0, len(result)-1):
            result[i].next = result[i+1]      
        
        return result[0]
