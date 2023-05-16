class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        quick = head

        for _ in range(n):
            if quick.next:
                quick = quick.next
            else:
                return head.next

        while quick and quick.next:
            quick = quick.next
            slow = slow.next
        slow.next = slow.next.next
        return head
