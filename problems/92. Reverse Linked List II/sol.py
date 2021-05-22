# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        # base case i.e when no head or 1 node or left==right
        if head==None or head.next==None or left==right:
            return head
        
        
        # we are creating dummy bcz we need pointer to node just prior to left (in one case when left = 1 ,we need it)
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        
        pos=1

        while pos<=left-1:
            pre=pre.next
            pos+=1
        # if we take ex-1 
        # pre points as dummyNode->(pre==1)->2->3->4->5->None
        
        # reverse nodes from m to n positions
        prev = None
        curr = pre.next
        pos=1
        while pos<=right-left+1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            pos+=1
        # now as in ex-1
        # dummyNode->(prev==4)->3->2->None
        
        pre.next = prev
        # dummyNode->(pre->1)->4->3->2->None
        
        
        # Now we are going to the last node of reversed linked list
        while prev.next:
            prev=prev.next
        
        prev.next=curr
        # dummyNode->(pre->1)->4->3->2->5->None
        

        return dummyNode.next
    
                                                                                                
                                                                                        
                                                                            # OR
    
   
    
    # slight modification in previous code and we dont need to run last while loop !!!! V.V.I
    
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        # base case i.e when no head or 1 node or left==right
        if head==None or head.next==None or left==right:
            return head
        
        
        # we are creating dummy bcz we need pointer to node just prior to left (in one case when left = 1 ,we need it)
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        
        pos=1

        while pos<left:
            pre=pre.next
            pos+=1
        
        # if we take ex-1 
        # pre points as dummyNode->(pre==1)->2->3->4->5->None
        
        tail=pre.next # by this we will keep track of the last node in reversed list
        # here in ex-1 tail will always points to node 2 i.e node at left position
        
        # reverse nodes from m to n positions
        prev = None
        curr = pre.next
        pos=1
        while pos<=right-left+1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            pos+=1
        # now as in ex-1
        # dummyNode->(prev==4)->3->2->None
        
        pre.next = prev
        # dummyNode->(pre->1)->4->3->2->None
        
        
        tail.next=curr
        # dummyNode->(pre->1)->4->3->2->5->None
        

        return dummyNode.next
        
