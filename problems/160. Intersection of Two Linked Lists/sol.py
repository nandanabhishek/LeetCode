# Approach - 1 : best one



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if not headA or not headB:
            return None
        
        currA, currB = headA, headB
        
        while currA != currB:
            currB = headA if currB is None else currB.next
            currA = headB if currA is None else currA.next
            
        return currA
            
            
            
        




# Approach - 2:




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # base case
        if headA == None or headB == None:
            return None
        
        curA = headA
        curB = headB
        
        lenA = 0
        lenB = 0
        
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
            
        curA = headA
        curB = headB
        
        if lenA > lenB: # the idea is to make the curA at the position from where they can meet in same no. of steps
            for i in range(lenA-lenB):
                curA = curA.next
        if lenB > lenA: # the idea is to make the curB at the position from where they can meet in same no. of steps
            for i in range(lenB-lenA):
                curB = curB.next
                
        while curB != curA:
            curB = curB.next
            curA = curA.next
            
        return curA
           
