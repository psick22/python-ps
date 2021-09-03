def solution(board, r, c):




    answer = 0
    return answer


boards = [
    [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]],
    [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
]
rr = [1, 0]
cc = [0, 1]

for i, (b, r, c) in enumerate(zip(boards, rr, cc)):
    print(solution(b, r, c))
