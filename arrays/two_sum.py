# LeetCode 1: Two Sum
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i , num in enumerate(nums):
            complement = target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
