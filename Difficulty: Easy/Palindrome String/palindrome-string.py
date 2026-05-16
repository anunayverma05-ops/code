class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Using two-pointer approach for optimal O(1) auxiliary space
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
