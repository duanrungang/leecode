class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """是否有环"""
        slow = head
        quick = head
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False
