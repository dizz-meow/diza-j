from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Compute prefix sums
        # P[i] stores the sum of nums[0] to nums[i-1]
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            
        # Step 2: Monotonic Deque to find the shortest valid subarray
        # It stores indices of the prefix sum array P
        dq = deque()
        min_len = float('inf')
        
        for i in range(n + 1):
            # Check if we found a valid subarray with sum >= k
            while dq and P[i] - P[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
                
            # Maintain increasing order of values in the deque
            # If P[i] <= P[last element], the older element is less useful
            while dq and P[i] <= P[dq[-1]]:
                dq.pop()
                
            # Add current index to the deque
            dq.append(i)
            
        return min_len if min_len != float('inf') else -1
