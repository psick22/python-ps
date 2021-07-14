import itertools as it
import re


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2


def solution(expression):
    # [+, -, *]
    operators = ['+', '-', '*']
    used_ops = set()
    pointer = 0
    equation = []
    for i in range(len(expression)):
        if expression[i] in operators:
            equation.append(expression[pointer:i])
            equation.append(expression[i])
            used_ops.add(expression[i])
            pointer = i + 1
        if i == len(expression) - 1:
            equation.append(expression[pointer:])
    permutations = list(it.permutations(used_ops))
    # print(equation)
    answer = []
    for perm in permutations:
        temp = equation.copy()
        # print('==============우선순위:', perm)
        for operator in perm:
            idx = 0
            while len(temp) > idx:
                # print('temp', temp)
                # print('idx', idx)
                # print('operator', operator)
                if temp[idx] == operator:
                    res = calculate(int(temp[idx - 1]), int(temp[idx + 1]), temp[idx])
                    temp = temp[0:idx - 1] + [res] + temp[idx + 2:]
                    idx -= 1
                else:
                    idx += 1
        answer.append(abs(int(temp[0])))
    return max(answer)


params = [
    "100-200*300-500+20", "50*6-3*2"
]

for p in params:
    print(f'({params.index(p)}): {solution(p)}')
