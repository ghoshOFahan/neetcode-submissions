# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        k=0;
        while temp!=None:
            temp=temp.next
            k+=1
        temp=head
        k=k-n
        if k==0:
            return head.next
        temp = head
        for i in range(k-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
            
