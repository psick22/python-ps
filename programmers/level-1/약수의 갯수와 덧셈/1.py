# 10:33 ~ 10:39
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                cnt += 1
        if (cnt + 1) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


left = 13
right = 17
print(solution(left, right))
