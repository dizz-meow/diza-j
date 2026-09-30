def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
        
    slow = 0  # Tracks the position of the unique elements
    
    # 'fast' explores the array ahead
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast] # Modify array in-place
            
    return slow + 1
