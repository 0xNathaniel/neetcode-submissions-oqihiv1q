# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def countDiameter(root):
            if not root.left and not root.right:
                return (0, 0)
            
            if not root.left and root.right:
                (main, alt) = countDiameter(root.right)
                return (main + 1, alt)

            if root.left and not root.right:
                (main, alt) = countDiameter(root.left)
                return (main + 1, alt)

            if root.left and root.right:
                (left_len, alt_left) = countDiameter(root.left)
                (right_len, alt_right) = countDiameter(root.right)

                main = 1 + max(left_len, right_len)

                alt_this = (1 + left_len) + (1 + right_len)
                alt = max(alt_this, max(alt_right, alt_left))

                return (main, alt)

        (main, alt) =  countDiameter(root)
        return max(main, alt)