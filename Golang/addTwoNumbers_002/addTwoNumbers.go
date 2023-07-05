package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{} // 哨兵节点
	cur := dummy
	carry := 0 // 进位
	for l1 != nil || l2 != nil || carry != 0 {
		if l1 != nil {
			carry += l1.Val // 节点值和进位加在一起
		}
		if l2 != nil {
			carry += l2.Val // 节点值和进位加在一起
		}
		cur.Next = &ListNode{Val: carry % 10}
		carry /= 10    // 新的进位
		cur = cur.Next // 下一个节点
		if l1 != nil {
			l1 = l1.Next // 下一个节点
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}
	return dummy.Next
}
