def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = bin(i | j)[2:].rjust(n, "0")
        temp = temp.replace("1", "#").replace("0", " ")
        answer.append(temp)

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
