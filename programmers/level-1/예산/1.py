# 16:30~16:34

def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            return answer
        answer += 1

    return answer


d = [2, 2, 3, 3]
budget = 10
print(solution(d, budget))
