# 17:33~17:41~
def solution(skill, skill_trees):
    answer = 0
    res = []
    for tree in skill_trees:
        for char in skill:
            idx = tree.index(char)
            if tree[0]

    return answer


skill = ["CBD"]
skill_trees = [["BACDE", "CBADF", "AECB", "BDA"]]
for i, (s1, s2) in enumerate(zip(skill, skill_trees)):
    print(f'case {i + 1} : {solution(s1, s2)}')
