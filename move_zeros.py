def move_zeros(nums):
    zero_count = 0  # variable to keep track of the number of zeros
    
    # Iterate through the array and move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i-zero_count] = nums[i]
        else:
            zero_count += 1
    
    # Fill the end of the array with zeros
    for i in range(len(nums)-zero_count, len(nums)):
        nums[i] = 0
    
    return nums

nums = [0, 1, 0, 3, 12]
result = move_zeros(nums)
print(result)
