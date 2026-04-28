class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sol, visited = [], [0] * n
        permutation_map = {}

        def backtrack(level):
            if level > n:
                permutation_map[tuple(sol)] = True
                return

            for i in range(n):
                if visited[i]:
                    continue

                sol.append(nums[i])
                visited[i] = 1
                backtrack(level + 1)
                visited[i] = 0
                sol.pop()
            
        backtrack(1)
        return [list(key) for key in permutation_map.keys()]