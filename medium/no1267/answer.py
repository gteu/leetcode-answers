class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, columns = set(), set()
        for i in range(m):
            count = 0
            for j in range(n):
                count += grid[i][j] == 1
                if count > 1:
                    rows.add(i)
                    break
        
        for j in range(n):
            count = 0
            for i in range(m):
                count += grid[i][j] == 1
                if count > 1:
                    columns.add(j)
                    break
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i in rows or j in columns):
                    ans += 1
        
        return ans
