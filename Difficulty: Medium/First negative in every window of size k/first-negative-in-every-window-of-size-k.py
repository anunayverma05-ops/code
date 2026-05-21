from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        n = len(arr)
        result = []
        neg_indices = deque()
        
        
        for i in range(k):
            if arr[i] < 0:
                neg_indices.append(i)
        
        
        for i in range(k, n):

            if neg_indices:
                result.append(arr[neg_indices[0]])
            else:
                result.append(0)
                

            while neg_indices and neg_indices[0] <= i - k:
                neg_indices.popleft()
                

            if arr[i] < 0:
                neg_indices.append(i)
        

        if neg_indices:
            result.append(arr[neg_indices[0]])
        else:
            result.append(0)
            
        return result