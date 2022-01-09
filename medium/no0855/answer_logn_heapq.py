# This is a solution using priority queue.
# heappop and heappush take O(logN), so it's faster than the linear solution.
# Note that deletion is quite difficult for heap algorithm, so lazy deletion will be a key.
# https://docs.python.org/ja/3/library/heapq.html 

from heapq import heappop, heappush

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seated = []
        self.avail_first = {}
        self.avail_last = {}
        self.put_segment(0, self.n - 1)
    
    def put_segment(self, first, last):
        if first == 0 or last == self.n - 1:
            pr = last - first
        else:
            pr = (last - first) // 2
        segment = [-pr, first, last, True]
        self.avail_first[first] = segment
        self.avail_last[last] = segment
        heappush(self.seated, segment)
        
    def seat(self) -> int:
        while True:
            _, first, last, is_valid = heappop(self.seated)
            
            if is_valid:
                del self.avail_first[first]
                del self.avail_last[last]
                break
                
        if first == 0:
            ret = 0
            if first != last:
                self.put_segment(first + 1, last)
        elif last == self.n - 1:
            ret = last
            if first != last:
                self.put_segment(first, last - 1)
        else:
            ret = (first + last) // 2
            if ret > first:
                self.put_segment(first, ret - 1)
            if ret < last:
                self.put_segment(ret + 1, last)
        
        return ret
          
    def leave(self, p: int) -> None:
        first, last = p, p
        left, right = p - 1, p + 1
        
        if left >= 0 and left in self.avail_last:
            segment_left = self.avail_last.pop(left)
            segment_left[3] = False
            first = segment_left[1]
            
        if right < self.n and right in self.avail_first:
            segment_right = self.avail_first.pop(right)
            segment_right[3] = False
            last = segment_right[2]
    
        self.put_segment(first, last)
    