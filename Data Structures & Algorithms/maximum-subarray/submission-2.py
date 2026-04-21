class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sub = max(cur_sum, max_sub)

        return max_sub