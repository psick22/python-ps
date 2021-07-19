# 13:39~
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dis = [[0] * m for _ in range(n)]
    dq = deque()
    dq.append((0, 0))
    dis[0][0] = 1
    while dq:
        if dis[n - 1][m - 1] != 0:
            return dis[n - 1][m - 1]

        temp = dq.popleft()
        for direction in range(4):
            x = temp[0] + dx[direction]
            y = temp[1] + dy[direction]
            if 0 <= x <= n - 1 and 0 <= y <= m - 1 and maps[x][y] == 1:
                if dis[x][y] == 0:
                    maps[temp[0]][temp[1]] = 0
                    dq.append((x, y))
                    dis[x][y] = dis[temp[0]][temp[1]] + 1

    if dis[n - 1][m - 1] == 0:
        return -1


maps = [
    [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]],
    [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
]

results = [
    11, -1
]

for i, m in enumerate(maps):
    print(f'case {i + 1} : {solution(m)}')
