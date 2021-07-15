# 16:05~ 16:57
def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt += 1
    for x1, y1, x2, y2 in queries:
        temp = [row[y1 - 1:y2] for row in board[x1 - 1:x2]]
        temp_rows, temp_cols = len(temp), len(temp[0])
        res = 2147000000

        for a in range(temp_rows):
            for b in range(temp_cols):
                na = a + x1 - 1
                nb = b + y1 - 1
                if a == 0 and b != 0:
                    board[na][nb] = temp[a][b - 1]
                    res = min(board[na][nb], res)

                elif b == 0 and a != temp_rows - 1:
                    board[na][nb] = temp[a + 1][b]
                    res = min(board[na][nb], res)

                elif a == temp_rows - 1 and b != temp_cols - 1:
                    board[na][nb] = temp[a][b + 1]
                    res = min(board[na][nb], res)

                elif b == temp_cols - 1 and a != 0:
                    board[na][nb] = temp[a - 1][b]
                    res = min(board[na][nb], res)

                else:
                    board[na][nb] = temp[a][b]
        answer.append(res)

    return answer


rows = [6, 3, 100]
columns = [6, 3, 97]
queries = [
    [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]],
    [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]],
    [[1, 1, 100, 97]]

]

for idx, (v, c, q) in enumerate(zip(rows, columns, queries)):
    print(f'case {idx + 1} : {solution(v, c, q)}')
    print('======================================')

results = [
    [8, 10, 25],
    [1, 1, 5, 3],
    [1]
]
