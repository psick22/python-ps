# 10: 05~ 10:42
from collections import deque


def solution(N, road, K):
    board = [[0] * (N + 1) for _ in range(N + 1)]
    times = [2147000000 for _ in range(N + 1)] # 최소 시간
    for a, b, c in road:
        if board[a][b] == 0 and board[b][a] == 0:
            board[a][b] = c
            board[b][a] = c
        else:
            if c < board[a][b]:
                board[a][b] = c
                board[b][a] = c

    dq = deque()
    dq.append(1)
    times[1] = 0

    while dq:
        temp = dq.popleft()
        for i in range(1, len(board)):
            # temp -> i
            if board[temp][i] != 0:
                if times[i] > times[temp] + board[temp][i] and times[temp] + board[temp][i] <= K:
                    times[i] = times[temp] + board[temp][i]
                    dq.append(i)

    cnt = 0
    for x in times:
        if x <= K:
            cnt += 1

    return cnt


nn = [5, 6]
roads = [
    [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
    [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
]
kk = [3, 4]
results = [
    4, 4
]

for i, (n, r, k) in enumerate(zip(nn, roads, kk)):
    print(f"{i + 1} : {solution(n, r, k)}")
