class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class CircleLinkedList:
    """循环链表"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def nodeLength(self):
        """链表长度"""
        if self.isEmpty():
            return 0
        count = 1
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def addNode(self, val: int):
        """头部添加元素"""
        newNode = ListNode(val)
        if self.head is not None:
            newNode.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode
            newNode.next = self.head
        self.head = newNode

    def appendNode(self, val: int):
        """尾部添加元素"""
        newNode = ListNode(val)
        if self.head is not None:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head
        else:
            self.head = newNode
            newNode.next = self.head

    def addNodeLoc(self, loc: int, val):
        """指定位置插入元素"""
        if loc <= 0:
            self.addNode(val)
        elif loc > self.nodeLength() - 1:
            self.appendNode(val)
        else:
            newNode = ListNode(val)
            cur = self.head
            for _ in range(loc-1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode

    def removeNode(self, val):
        """删除节点"""
        # 如果链表为空直接返回
        if self.isEmpty():
            return
        cur = self.head
        pre = ListNode
        # 如果第一个元素为需要删除的元素
        if cur.val == val:
            if cur.next != self.head:
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
                self.head = self.head.next
            # 如果只有一个元素
            else:
                self.head = None
        # 如果删除的是链表中间的元素
        else:
            pre = self.head
            while cur.next != self.head:
                if cur.val == val:
                    pre.next = cur.next
                    return True
                else:
                    pre = cur
                    cur = cur.next
        # 如果删除的是结尾的元素
        if cur.val == val:
            pre.next = self.head
            return True

    def printNode(self):
        """输出链表节点"""
        cur = self.head
        while cur.next != self.head:
            print(cur.val, end='-->')
            cur = cur.next
        print(cur.val, end='-->')
        print('None')

    def searchNode(self, val):
        """查找节点存不存在"""
        cur = self.head
        while cur.next != self.head:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    circleList = CircleLinkedList()
    for i in range(6):
        circleList.appendNode(i)
    circleList.printNode()          # 0-->1-->2-->3-->4-->5-->None
    circleList.addNode(10)
    circleList.printNode()          # 10-->0-->1-->2-->3-->4-->5-->None
    circleList.removeNode(2)
    circleList.printNode()          # 10-->0-->1-->3-->4-->5-->None
    circleList.addNodeLoc(3, 2)
    circleList.printNode()          # 10-->0-->1-->2-->3-->4-->5-->None
    print(circleList.searchNode(0))  # True


