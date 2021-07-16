from collections import deque


def solution(dartResult):
    score = []
    arr = []
    scoreMap = {
        "S": 1,
        "D": 2,
        "T": 3,
    }
    res = []
    tmp = 0
    for idx, char in enumerate(dartResult):
        if char.isdigit() and idx != 0:
            if char == '0' and dartResult[idx - 1] == '1':
                continue
            arr.append(dartResult[tmp:idx])
            tmp = idx

        if idx == len(dartResult) - 1:
            arr.append(dartResult[tmp:])
    for cmd in arr:
        temp = [0, 0, 0]  # score, bonus, option
        bias = 0
        if cmd[0] == '1' and cmd[1] == '0':
            bias = 1

        temp[0] = int(cmd[0:bias + 1])
        temp[1] = scoreMap[cmd[1 + bias]]

        if (bias == 0 and len(cmd) == 2) or (bias == 1 and len(cmd) == 3):
            temp[2] = 0
        else:
            temp[2] = cmd[-1]

        res.append(temp)

    for idx, x in enumerate(res):
        if x[2] == 0:
            score.append(x[0] ** x[1])
        else:
            if x[2] == "*":
                if idx != 0:
                    score[idx - 1] *= 2
                score.append((x[0] ** x[1]) * 2)
            elif x[2] == "#":
                score.append(-1 * (x[0] ** x[1]))

    return sum(score)


dartResult = "1D2S0T"

print(solution(dartResult))
