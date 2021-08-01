def compare(number, target):
    cnt = 0
    length = len(number)
    str1 = number
    str2 = target
    if len(number) != len(target):
        str1 = max(number, target, key=len)
        str2 = min(number, target, key=len)
        diff = "0" * (len(str1) - len(str2))
        str2 = diff + str2
        length = len(str1)

    for i in range(length - 1, -1, -1):
        if str1[i] != str2[i]:
            cnt += 1
            if cnt >= 3:
                return False

    if cnt == 0:
        return False

    else:
        return True


def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            num_bin = bin(number).lstrip("0b")
            i = number + 1
            flag = True
            while flag:
                if compare(num_bin, bin(i).lstrip("0b")):
                    answer.append(i)
                    flag = False
                i += 1

    return answer


numbers = [2, 7]
results = [3, 11]

print(solution(numbers))
