# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        while temp!=None:
            length+=1
            temp=temp.next
        length=length-n
        if length==0:
            return head.next
        temp=head
        for i in range(length-1):
            temp=temp.next
        temp.next=temp.next.next
        return head