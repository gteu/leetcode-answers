# This is another solution using bit manipulation.
# The difference is that it gradually shifts answer to the left by each digit.

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans