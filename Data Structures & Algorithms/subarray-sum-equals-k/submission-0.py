class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        total, res = 0, 0

        for num in nums:
            total += num

            if total - k in sums:
                res += sums[total - k]

            sums[total] = sums.get(total, 0) + 1

        return res