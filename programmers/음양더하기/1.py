def solution(absolutes, signs):
    sum = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            sum += num
        else:
            sum -= num
    return sum


absolutes = [4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))
