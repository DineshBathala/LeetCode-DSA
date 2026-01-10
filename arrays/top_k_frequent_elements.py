# LeetCode 347: Top K Frequent Elements
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency
        freq = Counter(nums)

        # Step 2: Sort by frequency (descending)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Take first k elements
        result = []
        for i in range(k):
            result.append(sorted_freq[i][0])

        return result

        
