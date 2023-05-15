class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BilateralLinkList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """判断链表是否为空"""
        return self.head is None

    def nodeLength(self):
        """链表的长度"""
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def addNode(self, val):
        """在头部添加元素"""
        newNode = ListNode(val)

        # 当链表为空时
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def appendNode(self, val):
        """尾部添加元素"""
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur

    def addNodeLoc(self, loc: int, val):
        """指定位置插入元素"""
        if loc <= 0:
            self.addNode(val)
        elif loc > self.nodeLength() - 1:
            self.appendNode(val)
        else:
            cur = self.head
            newNode = ListNode(val)
            for _ in range(loc):
                cur = cur.next
            # 新节点的前一个节点指向当前节点的上一个节点
            newNode.prev = cur.prev
            # 新节点的下一个节点指向当前节点
            newNode.next = cur
            # 当前节点的上一个节点指向新节点
            cur.prev.next = newNode
            # 当前节点的向上指针指向新节点
            cur.prev = newNode

    def removeNode(self, val):
        if self.isEmpty():
            return
        cur = self.head
        # 删除的元素为第一个元素
        if cur.val == val:
            # 如果只有一个元素
            if cur.next is None:
                self.head = None
                return True
            else:
                self.head = cur.next
                cur.next.prev = None
                return True

        while cur.next is not None:
            if cur.val == val:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            cur = cur.next

        # 删除元素在最后一个
        if cur.val == val:
            cur.prev.next = None
            return True

    def printNode(self):
        """输出链表节点"""
        cur = self.head
        while cur is not None:
            print(cur.val, end='-->')
            cur = cur.next
        print("None")

    def searchNode(self, val):
        """查找节点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    bilateralLinkList = BilateralLinkList()
    for i in range(6):
        bilateralLinkList.appendNode(i)
    bilateralLinkList.printNode()       # 0-->1-->2-->3-->4-->5-->None
    bilateralLinkList.addNode(10)
    bilateralLinkList.printNode()       # 10-->0-->1-->2-->3-->4-->5-->None
    bilateralLinkList.removeNode(2)
    bilateralLinkList.printNode()       # 10-->0-->1-->3-->4-->5-->None
    bilateralLinkList.addNodeLoc(3, 2)
    bilateralLinkList.printNode()       # 10-->0-->1-->2-->3-->4-->5-->None
