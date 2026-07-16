# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.inorder(root, out)
        return out
    
    def inorder(self, node: Optional[TreeNode], out: List[int]):
        if node is None:
            return
        self.inorder(node.left, out)
        out.append(node.val)
        self.inorder(node.right, out)


        