# 22:25~22:42
def solution(n, a, b):
    answer = 1
    if a % 2 == 0:
        a_pair = a // 2
    else:
        a_pair = a // 2 + 1

    if b % 2 == 0:
        b_pair = b // 2
    else:
        b_pair = b // 2 + 1

    while a_pair != b_pair:
        a_pair = (a_pair + 1) // 2
        b_pair = (b_pair + 1) // 2
        answer += 1

    return answer


n = 8
a = 4
b = 7
print(solution(n, a, b))
