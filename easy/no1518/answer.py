class Solution:
    def numWaterBottles(self, n_bottle: int, n_ex: int) -> int:
        ans = 0
        n_empty = 0
        while(n_bottle):
            ans += n_bottle
            n_empty += n_bottle
            n_bottle = n_empty // n_ex
            n_empty = n_empty % n_ex
        return ans
            
