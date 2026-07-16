# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.preorder(root, out)
        return out
    
    def preorder(self, node: Optional[TreeNode], out: List[int]):
        if node is None:
            return
        out.append(node.val)
        self.preorder(node.left, out)        
        self.preorder(node.right, out)