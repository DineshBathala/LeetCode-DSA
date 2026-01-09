# LeetCode 242: Valid Anagram
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
