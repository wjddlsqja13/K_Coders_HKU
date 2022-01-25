# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = dummy = ListNode()
        l = r = node.next = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                cur, prev = l, r
                for _ in range(k):
                    cur.next, cur, prev = prev, cur.next, cur
                node.next, node, l = prev, l, r
            else:
                return dummy.next
                

            