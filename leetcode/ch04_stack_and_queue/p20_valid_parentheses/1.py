class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for x in s:
            if x in map.values():
                stack.append(x)
            elif x in map.keys():
                if not stack or map[x] != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0


s = [
    "()[]{}",
    "(]"
]

for x in s:
    print(Solution().isValid(x))
