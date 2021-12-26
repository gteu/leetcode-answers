# Time complexity of this solution is O(N) but it requires for loop three times, which makes it slower.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left, right = [-1] * len(dominoes), [-1] * len(dominoes)
        cur_l, cur_r = False, False
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                cur_r = True
                right[i] = 0
            elif cur_r:
                right[i] = right[i-1] + 1
            if dominoes[i] == "L":
                cur_r = False
                
        for i in reversed(range(len(dominoes))):
            if dominoes[i] == "L":
                cur_l = True
                left[i] = 0
            elif cur_l:
                left[i] = left[i+1] + 1
            if dominoes[i] == "R":
                cur_l = False
                
        ans = ""
        for i in range(len(dominoes)):
            if left[i] == right[i]:
                ans += "."
            elif left[i] == -1:
                ans += "R"
            elif right [i] == -1:
                ans += "L"
            elif left[i] < right[i]:
                ans += "L"
            else:
                ans += "R"
        return ans
