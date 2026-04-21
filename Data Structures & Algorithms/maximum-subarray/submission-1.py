class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = -1001
        current_sum = 0
        n = len(nums)

        l = 0
        while l < n:
            if nums[l] <= 0:
                if nums[l] > largest:
                    largest = nums[l]
                l += 1
                continue

            current_sum = nums[l]
            r = l + 1

            while current_sum > 0:
                if current_sum > largest:
                    largest = current_sum

                if r >= n:
                    break

                current_sum += nums[r]
                r += 1

            l += 1

        return largest