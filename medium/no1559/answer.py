class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                stack = []
                stack.append((i, j, None, None))
                while(stack):
                    x, y, p_x, p_y = stack.pop()
                    if visited[x][y]:
                        if p_x is not None and p_y is not None:
                            return True
                    else:
                        visited[x][y] = True
                        for (n_x, n_y) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                            if 0 <= n_x < m and 0 <= n_y < n and grid[n_x][n_y] == grid[x][y]:
                                if not visited[n_x][n_y] or (p_x, p_y) != (n_x, n_y):
                                    stack.append((n_x, n_y, x, y))
        return False