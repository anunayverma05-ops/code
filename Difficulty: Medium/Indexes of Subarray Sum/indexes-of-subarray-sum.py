#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        start = 0
        current_sum = 0
        
        # Iterate through the array using 'end' as the right pointer
        for end in range(n):
            current_sum += arr[end]
            
            # Shrink the window from the left if current_sum exceeds target
            while current_sum > target and start < end:
                current_sum -= arr[start]
                start += 1
                
            # Check if we found the target sum
            if current_sum == target:
                # Problem requires 1-based indexing
                return [start + 1, end + 1]
                
        # If no subarray is found
        return [-1]