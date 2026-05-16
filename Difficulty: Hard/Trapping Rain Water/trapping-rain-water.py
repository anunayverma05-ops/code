class Solution:
    def maxWater(self, arr) -> int:
        # Base case: if array has fewer than 3 blocks, no water can be trapped
        if not arr or len(arr) < 3:
            return 0
            
        left = 0
        right = len(arr) - 1
        
        left_max = 0
        right_max = 0
        
        total_water = 0
        
        while left < right:
            if arr[left] <= arr[right]:
                if arr[left] >= left_max:
                    left_max = arr[left]
                else:
                    total_water += left_max - arr[left]
                left += 1
            else:
                if arr[right] >= right_max:
                    right_max = arr[right]
                else:
                    total_water += right_max - arr[right]
                right -= 1
                
        return total_water
        