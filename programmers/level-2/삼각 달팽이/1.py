def solution(n):
    answer = []
    cnt = 1
    board = [[0] * (r + 1) for r in range(n)]
    row = -1
    col = 0
    while n > 0:
        for _ in range(n):
            row += 1
            board[row][col] = cnt
            cnt += 1
        for _ in range(n - 1):
            col += 1
            board[row][col] = cnt
            cnt += 1
        for _ in range(n - 2):
            row -= 1
            col -= 1
            board[row][col] = cnt
            cnt += 1
        n -= 3

    for row in board:
        for x in row:
            answer.append(x)

    return answer


nn = [4, 5, 6]

for n in nn:
    print(solution(n))
