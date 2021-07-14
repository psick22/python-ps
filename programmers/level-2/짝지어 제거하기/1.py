def solution(s):
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    if len(stack) == 0:
        return 1
    else:
        return 0


s = "cdcd"
print(solution(s))
