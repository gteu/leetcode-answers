# Maximum subarray problem. This is a solution using Kadane's algorithm.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = -10**5
        for num in nums:
            cur = max(num, num + cur)
            best = max(cur, best)
        return best
