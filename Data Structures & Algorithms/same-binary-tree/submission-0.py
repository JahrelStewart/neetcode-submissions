# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_res, q_res = [], []
        p_res.insert(0 ,self.equalTree(p, p_res))
        q_res.insert(0, self.equalTree(q, q_res))
        return p_res == q_res
    
    def equalTree(self, root: Optional[TreeNode], res: List[int]):        
        if not root:
            return None
                
        res.append(self.equalTree(root.left, res))
        res.append(self.equalTree(root.right, res))    
        return root.val    

        