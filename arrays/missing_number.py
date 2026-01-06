# LeetCode 268: Missing Number
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1))-sum(nums)
