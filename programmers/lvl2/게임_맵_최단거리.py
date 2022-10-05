
from collections import deque

def solution(maps):
    answer = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(n, m):
        q = deque()
        q.append((n, m))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0)

    return answer if answer != 1 else -1
