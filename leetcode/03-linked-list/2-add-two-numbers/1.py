# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ''
        b = ''
        while l1:
            a = str(l1.val) + a
            l1 = l1.next

        while l2:
            b = str(l2.val) + b
            l2 = l2.next
        res = int(a) + int(b)
        answer = []
        for i in range(len(str(res)) - 1, -1, -1):
            answer.append(ListNode(int(str(res)[i]), None))

        for i in range(len(answer) - 1):
            answer[i].next = answer[i + 1]

        return answer[0]