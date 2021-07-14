def solution(board, moves):
    temp = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            data = board[j][i - 1]
            if data != 0:
                board[j][i - 1] = 0
                if len(temp) == 0:
                    temp.append(data)
                    break
                else:
                    if data == temp[-1]:
                        temp.pop()
                        answer += 2
                        break
                    else:
                        temp.append(data)
                        break

    return answer
