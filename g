def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1] # LeetCode 167 uses 1-based indexing
        elif current_sum < target:
            left += 1  # Need a larger sum, move left inward
        else:
            right -= 1 # Need a smaller sum, move right inward
            
    return []
