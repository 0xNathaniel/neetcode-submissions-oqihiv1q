class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        n = len(s)

        for i in range(n):
            memo[s[i]] = memo.get(s[i], 0) + 1

            # Expand oddly
            l, r = i - 1, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                memo[s[l : r + 1]] = memo.get(s[l : r + 1], 0) + 1
                l -= 1
                r += 1

            # Expand evenly
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                memo[s[l : r + 1]] = memo.get(s[l : r + 1], 0) + 1
                l -= 1
                r += 1

        return sum(memo.values())