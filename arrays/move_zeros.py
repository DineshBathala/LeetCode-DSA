# LeetCode 283 - Move Zeroes
# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                last_non_zero += 1
