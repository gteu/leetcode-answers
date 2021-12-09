class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        return self.dfs(maze, entrance)
            
    def dfs(self, maze, entrance):
        m = len(maze)
        n = len(maze[0])
        dist = [[-1] * n for i in range(m)]
        que = deque([entrance])
        dist[entrance[0]][entrance[1]] = 0
        while que:
            cx, cy = que.popleft()
            for i, j in [(1,0), (0,1), (-1,0), (0, -1)]:
                nx, ny =  cx + i, cy + j
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    pass
                elif nx == 0 or nx == m-1 or ny == 0 or ny == n-1:
                    if maze[nx][ny] == "." and dist[nx][ny] == -1:
                        return dist[cx][cy] + 1
                elif maze[nx][ny] == "+":
                    pass
                elif dist[nx][ny] == -1:
                    que.append([nx, ny])
                    dist[nx][ny] = dist[cx][cy] + 1
        return -1
