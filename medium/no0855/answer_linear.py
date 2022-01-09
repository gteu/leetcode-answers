# This is a quite straightforward and easy-to-understand solution, but time-complexity is O(N).
# To improve speed, we need to use another algorithm like priority queue (heapq).

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seated = []

    def seat(self) -> int:
        if not len(self.seated):
            res = 0
        else:
            res, maxd = 0, self.seated[0]
            for i in range(1, len(self.seated)):
                if (self.seated[i] - self.seated[i-1]) // 2 > maxd:
                    maxd = (self.seated[i] - self.seated[i-1]) // 2
                    res = (self.seated[i] + self.seated[i-1]) // 2
            if self.n - 1 - self.seated[-1] > maxd:
                maxd = self.n - 1 - self.seated[-1]
                res = self.n - 1
        bisect.insort(self.seated, res)
        return res
        
    def leave(self, p: int) -> None:
        self.seated.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
