import copy


def get_keys(key):
    temp = [key]
    for r in range(3):
        new_key = [[0] * len(key) for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                new_key[j][len(key) - 1 - i] = key[i][j]
        key = new_key
        temp.append(new_key)
    return temp


def can_open(board, key, lenK, lenL, i, j):
    s = lenK - 1
    e = lenK - 1 + lenL - 1 + 1
    for c in range(i, i + lenK):
        for d in range(j, j + lenK):
            if s <= c < e and s <= d < e:
                board[c][d] += key[c - i][d - j]

    for x in range(s, e):
        for y in range(s, e):
            if board[x][y] != 1:
                return False

    return True


def solution(key, lock):
    max_len = (len(key) - 1) * 2 + len(lock)
    board = [[0] * max_len for _ in range(max_len)]
    for a in range(len(lock)):
        for b in range(len(lock)):
            board[a + len(key) - 1][b + len(key) - 1] = lock[a][b]
    keys = get_keys(key)

    for k in keys:
        for i in range(len(key) - 1 + len(lock)):
            for j in range(len(key) - 1 + len(lock)):
                if can_open(copy.deepcopy(board), k, len(key), len(lock), i, j):
                    return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]

lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
