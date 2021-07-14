# 10:45~ 10:49
def solution(numbers):
    n = len(numbers)
    s = set()
    for i in range(n):
        for j in range(i + 1, n):
            s.add(numbers[i] + numbers[j])
    return sorted(list(s))


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
