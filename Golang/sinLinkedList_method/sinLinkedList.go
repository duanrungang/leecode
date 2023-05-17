package main

import "fmt"

type Object interface{}

type Node struct {
	data Object
	next *Node
}

type List struct {
	headNode *Node
}

func NewNode(data Object, next *Node) *Node {
	return &Node{data, next}
}

// IsEmpty 是否为空
func (list *List) IsEmpty() bool {
	return list.headNode == nil
}

// Length 计算链表长度
func (list *List) Length() int {
	var length int
	curNode := list.headNode
	for curNode != nil {
		length++
		curNode = curNode.next
	}
	return length
}

// AddNode 头部增加节点
func (list *List) AddNode(node *Node) *List {
	headNode := list.headNode
	if headNode.next != nil {
		node.next = headNode.next
	}
	headNode.next = node
	return list
}

// AppendNode 尾部增加节点
func (list *List) AppendNode(node *Node) *List {
	if list.IsEmpty() {
		list.headNode = node
		return list
	}
	curNode := list.headNode
	for curNode.next != nil {
		curNode = curNode.next
	}
	curNode.next = node
	return list
}

// AddNodeLoc 对应位置增加节点
func (list *List) AddNodeLoc(loc int, data Object) {
	if loc >= 0 && loc < list.Length() {
		count := 0
		if !list.IsEmpty() {
			curNode := list.headNode
			for curNode != nil && count < loc {
				count++
				curNode = curNode.next
			}
			node := NewNode(data, curNode.next)
			curNode.next = node
		}
	}
}

// RemoveNode 根据loc下标移除节点
func (list *List) RemoveNode(loc int) {
	if loc >= 0 && loc < list.Length() {
		count := 0
		if !list.IsEmpty() {
			curNode := list.headNode
			for curNode != nil && count < loc-1 {
				count++
				curNode = curNode.next
			}
			curNode.next = curNode.next.next
		}
	}
}

// PrintList 遍历链表
func PrintList(list *List) {
	cur := list.headNode
	for cur != nil {
		fmt.Println(cur.data)
		cur = cur.next
	}
}

// ReverseList 翻转链表
func ReverseList(head *Node) *Node {
	cur := head
	var pre *Node = nil
	for cur != nil {
		pre, cur, cur.next = cur, cur.next, pre
	}
	return cur
}

func main() {
	fmt.Println("NewNode======================")
	node := NewNode(1, nil)
	fmt.Println(node.data)
	list := &List{node}
	PrintList(list)
	node2 := NewNode("a", nil)
	list.AppendNode(node2)
	fmt.Println("AddNode======================")
	PrintList(list)
	node1 := NewNode(2, nil)
	list.AddNode(node1)
	fmt.Println("Length======================")
	PrintList(list)
	fmt.Println(list.Length())
	fmt.Println("AddNodeLoc======================")
	list.AddNodeLoc(1, 4)
	PrintList(list)
	fmt.Println("RemoveNode======================")
	list.RemoveNode(2)
	PrintList(list)
	fmt.Println("ReverseList=====================")
	ReverseList(node)
	PrintList(list)
}
