# If you use brute-force algorithm, it would take O(N^2) to solve this.
# You can make use of the fact that if you accumulate values by bitwise OR operation there are at most only 30 (the number of bits) different values.
# The resulting time-complexity is O(30N).

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res, cur = set(), set()
        for i in arr:
            cur = {j | i for j in cur} | {i}
            res |= cur
        return len(res)
