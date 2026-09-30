from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
        
        result = []
        q = deque() # Stores indices of elements
        
        for i, num in enumerate(nums):
            # 1. Remove the index that has slid out of the current window bounds
            if q and q[0] == i - k:
                q.popleft()
                
            # 2. Remove smaller elements from the back of the queue
            # Maintain a strictly decreasing order of values in the deque
            while q and nums[q[-1]] <= num:
                q.pop()
                
            # 3. Add the current element's index
            q.append(i)
            
            # 4. The first element in the queue is always the max for the current window
            # Only start adding to the result once we've reached a full window of size k
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result


