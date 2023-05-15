class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class SinLinkedList:
    """单链表的方法"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        """判断链表是否为空"""
        return self.head is None

    def nodeLength(self):
        """返回链表的长度"""
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def addHead(self, val: int):
        """在头部添加元素"""
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def appendNode(self, val: int):
        """在尾部添加元素"""
        newNode = ListNode(val)
        if self.isEmpty():
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    def insertNode(self, loc: int, val: int):
        """在对应位置添加元素"""
        if loc <= 0:
            self.addHead(val)
        elif loc > (self.nodeLength() - 1):
            self.appendNode(val)
        else:
            newNode = ListNode(val)
            cur = self.head
            for _ in range(loc - 1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode

    def removeNode(self, val: int):
        """删除对应值的节点"""
        cur = self.head
        pre = None
        while cur is not None:
            if cur.val == val:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def printNode(self):
        """输出链表节点"""
        cur = self.head
        while cur is not None:
            print(cur.val, end='-->')
            cur = cur.next
        print('None')

    def searchNode(self, val: int):
        """查找节点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    linkList = SinLinkedList()
    for i in range(6):
        linkList.appendNode(i)
    linkList.printNode()  # 0-->1-->2-->3-->4-->5-->None
    print(linkList.searchNode(4))  # True
    linkList.removeNode(0)
    linkList.removeNode(3)
    linkList.printNode()  # 1-->2-->4-->5-->None
    linkList.insertNode(2, 3)
    linkList.printNode()  # 1-->2-->3-->4-->5-->None
    linkList.addHead(0)
    linkList.printNode()  # 0-->1-->2-->3-->4-->5-->None
    print(linkList.nodeLength())  # 6
