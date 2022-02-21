class Solution: 
    
    
    def deleteAlt(self, head):
        answer = head
        while answer != None and answer.next != None:
            answer.next = answer.next.next
            answer = answer.next
