# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         nums = []
#         for i in range(50):
#             for j in range(20):
#                 for k in range(15):
#                     nums.append(2**i * 3**j * 5 ** k)
#         nums.sort()
#         return nums[n-1]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        p2, p3, p5 = 0, 0, 0
        while n > 1:
            min_ugly = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            if min_ugly == ugly[p2]*2:
                p2 += 1
            if min_ugly == ugly[p3]*3:
                p3 += 1
            if min_ugly == ugly[p5]*5:
                p5 += 1
            n -= 1
            ugly.append(min_ugly)
        return ugly[-1]
