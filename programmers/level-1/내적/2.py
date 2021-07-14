def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])

a = [1]
b = [3]

print(solution(a, b))