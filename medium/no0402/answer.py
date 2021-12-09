# 桁 DP で解いたもの
# これだと O(N^2) で TLE する

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         dp = [[0] * (k + 1)  for i in range(len(num) + 1)]
#         for i in range(len(num)):
#             for j in range(k + 1):
#                 if j == 0:
#                     dp[i+1][j] = int(str(dp[i][j]) + num[i])
#                 else:
#                     dp[i+1][j] = min(int(str(dp[i][j]) + num[i]), dp[i][j-1])
#         return str(min(dp[len(num)]))

# 貪欲法

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for num in nums:
            while k > 0 and stack and num < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
            
