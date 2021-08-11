class Node:
    def __init__(self, name, money, ref):
        self.name = name
        self.money = money
        self.ref = ref


def solution(enroll, referral, seller, amount):
    answer = []
    nodes = {}

    for e in enroll:
        nodes[e] = Node(e, 0, None)

    for e, r in zip(enroll, referral):
        if r == '-':
            nodes[e].ref = '-'
        else:
            nodes[e].ref = nodes[r]

    for s, a in zip(seller, amount):
        curr = nodes[s]
        profit = 100 * a
        m2 = profit // 10
        m1 = profit - m2
        while curr.ref != "-":
            curr.money += m1
            curr = curr.ref
            if m2 // 10 == 0:
                m1 = m2
                break
            temp = m2 // 10
            m1 = m2 - temp
            m2 = temp

        curr.money += m1

    for k, v in nodes.items():
        answer.append(int(v.money))

    return answer

enrolls = [
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
]

referrals = [
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
]

sellers = [

    ["young", "john", "tod", "emily", "mary", "young"],
    ["young", "john", "tod", "emily", "mary", "young", "young"],
    ["sam", "emily", "jaimie", "edward"]
]

amounts = [
    [12, 4, 2, 5, 10],

    [12, 4, 2, 5, 10, 10],
    [2, 3, 5, 4]
]

results = [
    [360, 958, 108, 0, 450, 18, 180, 1080],
    [0, 110, 378, 180, 270, 450, 0, 0]
]

for i, (e, r, s, a) in enumerate(zip(enrolls, referrals, sellers, amounts)):
    print(f'{i + 1} : {solution(e, r, s, a)}')
