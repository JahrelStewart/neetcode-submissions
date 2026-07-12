# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """    
        if head is None:
            return
                        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i,j = 0,len(nodes)-1
        turn = 0
        while i < j:
            if turn%2 == 0:
                nodes[i].next = nodes[j]
                i += 1
            else:
                nodes[j].next = nodes[i]
                j -= 1

            turn += 1
        
        nodes[i].next = None







