class Solution:
    def getSecondLargest(self, arr):
        # Initialize largest and second largest with -1 
        # (since elements are positive integers >= 1)
        largest = -1
        second_largest = -1
        
        for num in arr:
            # If current element is greater than the largest element
            if num > largest:
                second_largest = largest
                largest = num
            # If current element is smaller than largest but greater than second largest
            elif num > second_largest and num != largest:
                second_largest = num
                
        return second_largest