def move(ptr, num, dir, answer):
    while num > 0:
        if dir == "D":
            ptr += 1
        else:
            ptr -= 1

        if answer[ptr] != "X":
            num -= 1

    return ptr


def solution(n, k, cmd):
    answer = ["O"] * n
    ptr = k
    deleted = []
    move_cnt = 0

    for c in cmd:
        x = c.split(' ')
        if x[0] == "D":
            move_cnt += int(x[1])
        elif x[0] == "U":
            move_cnt -= int(x[1])

        elif x[0] == 'C':
            if move_cnt >= 0:
                ptr = move(ptr, move_cnt, "D", answer)

            else:
                ptr = move(ptr, -move_cnt, "U", answer)

            move_cnt = 0
            answer[ptr] = "X"
            deleted.append(ptr)
            if ptr < n - 1:
                ptr = move(ptr, 1, "D", answer)
            else:
                ptr = move(ptr, 1, "U", answer)
        elif x[0] == 'Z':
            if move_cnt >= 0:
                ptr = move(ptr, move_cnt, "D", answer)

            else:
                ptr = move(ptr, -move_cnt, "U", answer)

            move_cnt = 0

            answer[deleted.pop()] = "O"

    answer = ''.join(answer)

    return answer


nn = [8, 8]
kk = [2, 2]

cmds = [["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"],
        ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]]

results = ["OOOOXOOO", "OOXOXOOO"]

for i, (n, k, cmd) in enumerate(zip(nn, kk, cmds)):
    print(f'case {i + 1} : {solution(n, k, cmd)}')
