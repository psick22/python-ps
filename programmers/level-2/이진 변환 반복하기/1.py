def solution(s):
    cnt1 = 0
    cnt2 = 0
    while True:
        temp = ''
        for char in s:
            if char == "0":
                cnt2 += 1
            else:
                temp += char
        cnt1 += 1
        if temp == "1":
            break
        else:
            s = bin(len(temp)).lstrip("0b")

    answer = [cnt1, cnt2]
    return answer


arr = ["110010101001", "01110", "1111111"]
results = [[3, 8], [3, 3], [4, 1]]
for s in arr:
    print(f'({arr.index(s)}): {solution(s)}')
