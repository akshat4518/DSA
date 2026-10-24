
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        count = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    queue = deque([(i, j)])
                    grid[i][j] = '0'

                    while queue:
                        r, c = queue.popleft()

                        for dr, dc in [(-1, 0), (1, 0),
                                       (0, -1), (0, 1)]:
                            nr = r + dr
                            nc = c + dc

                            if (0 <= nr < n and
                                0 <= nc < m and
                                grid[nr][nc] == '1'):

                                queue.append((nr, nc))
                                grid[nr][nc] = '0'

        return count
