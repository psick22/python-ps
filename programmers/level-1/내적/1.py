def solution(a, b):
    n = len(a)
    answer = 0
    for i in range(n):
        answer += a[i] * b[i]

    return answer


a = [1]
b = [3]

print(solution(a, b))