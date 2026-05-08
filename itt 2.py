def transform_list(nums):
    return tuple(x**2 if x % 2 == 0 else x**3 for x in nums)
print(transform_list([6, 7, 8, 9]))
