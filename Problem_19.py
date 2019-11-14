# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        deep=0
        a=head
        l=[]
        
        while a.next!=None:
            l.append(a.val)
            a=a.next
            deep=deep+1
        l.append(a.val)
        
        if len(l) == 1:
            return ListNode('')
        
        del l[deep - n +1]
        a=ListNode(l[-1])
        b=a
        for i in reversed(range((len(l)-1))):
            b=a
            a=ListNode(l[i])
            a.next=b
           
        return a
