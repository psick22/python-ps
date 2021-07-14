import math


def solution(w, h):
    if math.gcd(w, h) == 1:
        return (w * h) - (w + h - 1)
    cnt = 0

    def f(x) -> float:
        return (-h / w) * x + h

    temp = 0
    for i in range(w):
        cnt += (math.ceil(f(i)) - math.floor(f(i + 1)))
        if int(f(i + 1)) == f(i + 1):
            temp = i + 1
            break
    return (w * h) - ((w // temp) * cnt)


w = 8
h = 12
print(solution(w, h))
