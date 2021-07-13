# 20분
def cal_dis(pos, left, right):
    left_dis = abs(left[0] - pos[0]) + abs(left[1] - pos[1])
    right_dis = abs(right[0] - pos[0]) + abs(right[1] - pos[1])
    if left_dis == right_dis:
        return False
    elif left_dis > right_dis:
        return 'right'
    else:
        return 'left'


def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]
    keys = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    def find_pos(num):
        for i in range(4):
            for j in range(3):
                if keys[i][j] == num:
                    return [i, j]

    for num in numbers:
        if num in [1, 4, 7]:
            left = find_pos(num)
            answer += 'L'
        elif num in [3, 6, 9]:
            right = find_pos(num)
            answer += 'R'
        else:
            pos = find_pos(num)
            decision = cal_dis(pos, left, right)
            if not decision:
                if hand == 'right':
                    right = pos
                    answer += "R"
                else:
                    left = pos
                    answer += "L"
            else:
                if decision == 'right':
                    right = pos
                    answer += "R"
                else:
                    left = pos
                    answer += "L"

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
