# LeetCode 238: Product of Array Except Self
# Time: O(n)
# Space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Step 1: build prefix products
        prev_prod = 1
        for i in range(n):
            answer[i] = prev_prod
            prev_prod *= nums[i]

        # Step 2: build suffix products and multiply
        after_prod = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= after_prod
            after_prod *= nums[i]

        return answer

