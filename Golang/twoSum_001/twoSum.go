package main

import "fmt"

// 方法一:暴力枚举
func twoSum_1(nums []int, target int) []int {
	for i, num := range nums {
		for j := i+1; j < len(nums); j++ {
			if num+nums[j]==target{
				return []int{i,j}
			}
		}
	}
	return nil
}

// 方法二: hash表
func twoSum_2(nums []int, target int) []int {
	hashTable := map[int]int{}
	for i, x := range nums {
		if p, ok :=hashTable[target-x]; ok{
			return []int{p,i}
		}
		hashTable[x] = i
	}
	return nil
}

func main()  {
	data := []int{2, 7, 11, 15}
	result1 := twoSum_1(data, 9)
	result2 := twoSum_2(data, 9)
	fmt.Println(result1, result2)
}