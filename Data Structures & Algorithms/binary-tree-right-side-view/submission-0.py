# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.levelOrderView(root, 0, out)
        out = [x[len(x)-1] for x in out]
        return out

    def levelOrderView(self, node: Optional[TreeNode], level: int, out: List[List[int]]):
        if not node:
            return 
        if len(out) <= level:
            out.append([])
        out[level].append(node.val)

        self.levelOrderView(node.left, level+1, out)
        self.levelOrderView(node.right, level+1, out)
        