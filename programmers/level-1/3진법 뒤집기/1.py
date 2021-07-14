# 7분
def solution(n: int):
    answer = 0
    rev = ''
    while n > 0:
        n, mod = n // 3, n % 3
        rev += str(mod)
    for i in range(1, len(rev) + 1):
        answer += int(rev[-i]) * 3 ** (i - 1)
    return answer


n = 45
print(solution(n))
