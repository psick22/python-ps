def moveLeft(str, number):
    temp1 = str[:number]
    temp2 = str[number:]
    return temp2 + temp1


def isRight(str):
    map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for char in str:
        if char in map:
            stack.append(char)
        elif char in map.values():
            if len(stack) != 0 and char == map[stack[-1]]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0

    for x in range(len(s)):
        temp = moveLeft(s, x)
        if isRight(temp):
            answer += 1

    return answer


ss = [
    "[](){}", "}]()[{", "[)(]", "}}}"
]

results = [3, 2, 0, 0]

for s in ss:
    print(solution(s))
