# 14:19~ 15:28

def solution(places):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []

    def dfs(x, y, L, ch):
        if ch[0] == 1:
            return
        if L == 2:
            return
        else:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx <= 4 and 0 <= ny <= 4:
                    if board[nx][ny] == "P" and dis[nx][ny] == 0:
                        ch[0] = 1
                    elif board[nx][ny] == "O":
                        dis[nx][ny] = 1
                        dfs(nx, ny, L + 1, ch)

    for place in places:
        board = [list(place[row]) for row in range(5)]
        ch = [0]

        for i in range(5):
            for j in range(5):
                if board[i][j] == "P":
                    dis = [[0] * 5 for _ in range(5)]
                    dis[i][j] = 1
                    dfs(i, j, 0, ch)
        if ch[0] == 0:
            res.append(1)
        else:
            res.append(0)

    return res


places = [

    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
]

for p in places:
    print(f'({places.index(p)}): {solution(p)}')
    print('======================================')

results = [1, 0, 1, 1, 1]
