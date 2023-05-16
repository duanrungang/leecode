class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoList_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个有序链表-迭代"""
        head = ListNode(0)
        node = head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return head.next

    def mergeTwoList_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoList_2(l1.next, l2)
        else:
            l2.next = self.mergeTwoList_2(l1, l2.next)
            return l2
