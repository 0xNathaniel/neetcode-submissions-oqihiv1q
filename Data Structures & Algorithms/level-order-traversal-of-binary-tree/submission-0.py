# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cur_list = []
        q = deque([root])

        while q:
            length = len(q)

            while length > 0:
                cur_root = q.popleft()
                if not cur_root:
                    length -= 1
                    continue
                
                cur_list.append(cur_root.val)

                if cur_root.left:
                    q.append(cur_root.left)
                if cur_root.right:
                    q.append(cur_root.right)

                length -= 1
            
            if cur_list:
                res.append(cur_list.copy())
            cur_list = []

        return res
                
            




        