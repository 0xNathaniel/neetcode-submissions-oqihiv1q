# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def deleteNodeHelper(root, key):
            if not root:
                return None

            if (key < root.val):
                root.left = deleteNodeHelper(root.left, key)

            elif (key > root.val):
                root.right = deleteNodeHelper(root.right, key)

            elif (key == root.val):
                if not root.right and not root.left:
                    return None

                elif root.left and not root.right:
                    return root.left

                elif not root.left and root.right:
                    return root.right

                else:
                    curr = root.right

                    while curr.left:
                        curr = curr.left

                    del_key = curr.val
                    root = deleteNodeHelper(root, del_key)
                    root.val = del_key

            return root

        return deleteNodeHelper(root, key)