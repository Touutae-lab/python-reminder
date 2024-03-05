class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        
        while left < right and s[left] == s[right]:
            char_to_remove = s[left]
            while left <= right and s[left] == char_to_remove:
                left += 1
            while right >= left and s[right] == char_to_remove:
                right -= 1
        return max(0, right - left + 1)