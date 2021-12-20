# Naive DP solution takes O(MN^2) and it will get TLE in the end. 
# When you get each element of DP table, you don't need to calculate N times and you only need to calculate from left or right element.
# Once you calculate the maximum left and right, sum point[i] and maximum of left[i] and right[i].

class Solution:
    def left(self, row):
        for i in range(1, len(row)):
            row[i] = max(row[i-1] - 1, row[i])
        return row
        
    def right(self, row):
        for i in range(1, len(row)):
            row[len(row)-1-i] = max(row[len(row)-i] - 1, row[len(row)-1-i])
        return row
    
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = [0] * len(points[0])
        for point in points:
            left = self.left(ans)
            right = self.right(ans)
            for i in range(len(points[0])):
                ans[i] = point[i] + max(left[i], right[i])
            print(ans)
        return max(ans)
        
