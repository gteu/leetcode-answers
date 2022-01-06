# This is a solutions using prefix sum (= cumulative sum).

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return abs(max(nums) - min(nums))
