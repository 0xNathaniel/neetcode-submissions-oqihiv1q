class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol, n = {}, [], len(nums)
        nums.sort()

        def backtrack(i):
            if i >= n:
                res[tuple(sol)] = True
                return

            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            

        backtrack(0)

        return [list(key) for key in res.keys()]