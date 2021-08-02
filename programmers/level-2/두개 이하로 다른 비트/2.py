def solution(numbers):
    answer = []

    for number in numbers:
        if number == 0:
            answer.append(1)
            continue
        num_bin = bin(number).lstrip('0b')

        if num_bin[-1] == '0':
            answer.append(number + 1)
        else:
            i = len(num_bin) - 1
            cnt = 0
            flag = True
            while flag and i >= 0:
                if num_bin[i] == '1':
                    cnt += 1
                else:
                    flag = False
                i -= 1
            answer.append(number + 2 ** (cnt - 1))

    return answer


numbers = [3, 7]
results = [3, 11]

print(solution(numbers))
#
# 01111
#
# 10000
# 10001
# 10010
# 10011
# 10111
