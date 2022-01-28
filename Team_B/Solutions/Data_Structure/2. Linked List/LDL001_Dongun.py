# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ls = []
        
        for list in lists:
            node = list
            while node != None:
                ls.append(node.val)
                node = node.next
                
        ls.sort()
        
        ans = dummy = ListNode()
        for v in ls:
            ans.next = ListNode(v)
            ans = ans.next
            
        return dummy.next