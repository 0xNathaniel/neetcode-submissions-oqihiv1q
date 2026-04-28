class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, sol, count, n = [], [], 0, len(candidates)

        def backtrack(i):
            nonlocal count
            if i >= n or count >= target:
                if count == target:
                    result.append(sol.copy())
                return

            sol.append(candidates[i])
            count += candidates[i]
            backtrack(i + 1)
            count -= candidates[i]
            sol.pop()

            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1

            backtrack(j)

        backtrack(0)
        return result