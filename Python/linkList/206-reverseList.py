class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList_1(head):
    """翻转链表-通过迭代实现"""
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre


def reverseList_2(head):
    """翻转链表-通过递归实现"""
    if not head or not head.next:
        return head
    nextNode = reverseList_2(head.next)
    head.next.next = head
    head.next = None
    return nextNode


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    result = reverseList_2(node)
