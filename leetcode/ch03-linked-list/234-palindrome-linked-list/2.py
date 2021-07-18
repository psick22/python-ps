from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        rev = None

        while fast and fast.next:
            rev, rev.next, slow = slow, rev, slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev
