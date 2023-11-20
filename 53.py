class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        c = nums[0]
        for i in range(1, len(nums)):
            if c > 0:
                c += nums[i]
            else:
                c = nums[i]
            if max_sum < c:
                max_sum = c
        return max_sum
