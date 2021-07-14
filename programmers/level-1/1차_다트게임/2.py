def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'k')
    score = ['10' if i == 'k' else i for i in dartResult]

    maps = ["S", "D", "T"]
    i = -1
    for x in score:
        if x in maps:
            answer[i] **= (maps.index(x) + 1)
        elif x == '*':
            if i != 0:
                answer[i - 1] *= 2
            answer[i] *= 2
        elif x == '#':
            answer[i] *= (-1)
        else:
            answer.append(int(x))
            i += 1

    return sum(answer)


dartResult = "1D2S0T"

print(solution(dartResult))
