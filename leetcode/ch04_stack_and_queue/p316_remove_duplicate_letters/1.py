from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        lst = []
        for char in s:
            counter[char] -= 1
            if char in lst:
                continue
            while lst and char < lst[-1] and counter[lst[-1]] > 0:
                lst.pop()
            lst.append(char)

        return ''.join(lst)


s = ["bcabc", "cbacdcbc"]
for x in s:
    Solution().removeDuplicateLetters(x)
