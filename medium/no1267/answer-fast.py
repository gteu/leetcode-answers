# Once you get the locations of servers, you don't need to calculate O(M*N) for loop again.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, columns = [0] * m, [0] * n
        servers = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    servers.append((i,j))
                    rows[i] += grid[i][j]
                    columns[j] += grid[i][j]
            
        ans = 0
        for i, j in servers:
            ans += rows[i] + columns[j] > 2
                    
        return ans
