class Solution:
    def sumOfDigits(self, n):
        digit_sum = 0
        
        while n > 0:
            
            digit_sum += n % 10
            
            n = n // 10
            
        return digit_sum