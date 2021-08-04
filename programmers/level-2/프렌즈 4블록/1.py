# 1시간
def fall_down(m, n, board):
    for x in range(m - 1, -1, -1):
        for y in range(n):
            if board[x][y] == 0:
                temp = x
                while board[temp - 1][y] == 0 and temp - 1 >= 0:
                    temp -= 1
                if temp - 1 >= 0:
                    board[x][y] = board[temp - 1][y]
                    board[temp - 1][y] = 0


def cascade(m, n, board):
    dx = [0, 1, 1]
    dy = [1, 1, 0]
    target = set()

    for x in range(m):
        for y in range(n):
            temp = board[x][y]
            if temp != 0:
                ch = [(x, y)]
                ch_cnt = 0
                for direction in range(3):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    ch.append((nx, ny))
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == temp:
                        ch_cnt += 1
                if ch_cnt == 3:
                    for c in ch:
                        target.add(c)
    return target


def solution(m, n, board):
    new_board = [[0] * n for _ in range(m)]
    answer = 0

    for x in range(m):
        for y in range(n):
            new_board[x][y] = ord(board[x][y])
    while True:
        target = cascade(m, n, new_board)

        if len(target) == 0:
            break
        else:
            for xx, yy in target:
                new_board[xx][yy] = 0
            fall_down(m, n, new_board)
            answer += len(target)

    return answer


mm = [4, 6]
nn = [5, 6]
boards = [
    ["CCBDE", "AAADE", "AAABF", "CCBBF"],
    ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
]

for i, (m, n, b) in enumerate(zip(mm, nn, boards)):
    print(f"{i + 1} : {solution(m, n, b)}")
