from typing import List


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """暴力枚举"""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """hash表"""
        mapData = {}
        for i, num in enumerate(nums):
            if target - num in mapData:
                return [mapData[target - num], i]
            mapData[nums[i]] = i
        return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    obj = Solution()
    result1 = obj.twoSum_1(nums, 9)
    result2 = obj.twoSum_2(nums, 9)
    print(result1)
    print(result2)
