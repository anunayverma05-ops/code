class Solution:
    def longestUniqueSubstr(self, s: str) -> int:
        
        char_map = {}
        max_len = 0
        left = 0  
        
        
        for right in range(len(s)):
            current_char = s[right]
            
            
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            
            # Update or insert the last seen position of the character
            char_map[current_char] = right
            
          
            max_len = max(max_len, right - left + 1)
            
        return max_len