class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        

        current_window_sum = sum(arr[:k])
        max_sum = current_window_sum
        

        for i in range(k, n):
            
            current_window_sum += arr[i] - arr[i - k]
            
            
            max_sum = max(max_sum, current_window_sum)
            
        return max_sum