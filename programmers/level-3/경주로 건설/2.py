dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = float('inf')
N = 0
visited = []
costs = []


def dfs(x, y, dir, cost):
    global answer, costs, visited
    if costs[x][y] != float('inf') and costs[x][y] < cost:
        return
    costs[x][y] = min(costs[x][y], cost)
    if cost >= answer:
        return
    if x == N - 1 and y == N - 1:
        answer = min(answer, cost)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if dir == i or dir == -1:
                visited[nx][ny] = 1
                dfs(nx, ny, i, cost + 100)
                visited[nx][ny] = 0
            else:
                visited[nx][ny] = 1
                dfs(nx, ny, i, cost + 600)
                visited[nx][ny] = 0


def solution(board):
    global N, visited, costs
    N = len(board)

    visited = [[0] * N for _ in range(N)]
    costs = [[float('inf')] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                visited[i][j] = 1

    dfs(0, 0, -1, 0)
    return answer


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

print(solution(boards[1]))
