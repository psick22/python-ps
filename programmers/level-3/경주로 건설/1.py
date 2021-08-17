from collections import deque


def solution(board):
    N = len(board)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    dq = deque()
    dq.append([0, 0, 0, 0])
    while dq:
        x, y, dir, cost = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]



boards = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]

]

for b in boards:
    print(solution(b))
