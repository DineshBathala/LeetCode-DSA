# LeetCode 1365: How Many Numbers Are Smaller Than the Current Number
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in rank:
                rank[num] = i
        
        return [rank[num] for num in nums]
