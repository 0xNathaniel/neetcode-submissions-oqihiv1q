class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx, n = 0, len(nums)

        while True:
            if idx >= n - 1:
                return True

            if nums[idx] == 0:
                return False

            crt_count, count = 0, nums[idx]
            max_cnt, max_idx, cur_idx = -1, -1, idx + 1

            while cur_idx < n and crt_count < count:
                if max_cnt < cur_idx + nums[cur_idx]:
                    max_cnt = cur_idx + nums[cur_idx]
                    max_idx = cur_idx
                cur_idx += 1
                crt_count += 1

            idx = max_idx
