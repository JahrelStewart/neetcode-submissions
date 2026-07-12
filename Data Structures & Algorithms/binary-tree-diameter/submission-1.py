# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.maxDiameter(root)[1]

    def maxDiameter(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (0, 0)

        leftHeight, leftDiameter = self.maxDiameter(root.left)
        rightHeight, rightDiameter = self.maxDiameter(root.right)

        currentDiameter = leftHeight + rightHeight
        maxDiameterSoFar = max(leftDiameter, rightDiameter, currentDiameter)

        maxHeight = 1 + max(leftHeight, rightHeight)

        return (maxHeight, maxDiameterSoFar)
        