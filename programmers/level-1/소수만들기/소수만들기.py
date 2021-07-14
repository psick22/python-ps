def isPrime(k):
    ch = [0] * (k + 1)
    ch[1] = 1
    if k == 1:
        return True
    for i in range(2, k):
        if ch[i] == 1:
            continue
        if k % i != 0:
            ch[i] = 1
            m = 2
            while m * i <= k:
                ch[m * i] = 1
                m += 1
        else:
            return False
    return True


answer = 0


def solution(nums):
    n = len(nums)

    def dfs(L, s, sum):
        global answer
        if L == 3:
            if isPrime(sum):
                answer += 1


        else:
            for i in range(s, n):
                dfs(L + 1, i + 1, sum + nums[i])

    dfs(0, 0, 0)

    return answer


nums = [1, 2, 3, 4]
print(solution(nums))
