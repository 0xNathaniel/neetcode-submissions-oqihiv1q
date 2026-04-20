# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True

            if (root1 and not root2) or (not root1 and root2):
                return False

            if root1.val != root2.val:
                return False

            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
            

        def isSubtreeHelper(root, subRoot):
            if not root:
                return False

            if root.val == subRoot.val:
                if isSameTree(root, subRoot):
                    return True

            return isSubtreeHelper(root.left, subRoot) or isSubtreeHelper(root.right, subRoot)


        return isSubtreeHelper(root, subRoot)