def move_zeroes(nums):
    writer = 0
    
    # Pass 1: "Reader" scans the list
    for reader in range(len(nums)):
        if nums[reader] != 0:
            # Move non-zero to the writer's position
            nums[writer] = nums[reader]
            writer += 1
            
    # Pass 2: Fill the remaining spots with zeros
    while writer < len(nums):
        nums[writer] = 0
        writer += 1

# Example
list11 = [1, 0, 2, 0, 0, 6, 3, 0, 4, 0, 5]
move_zeroes(list11)
print(list11) # [1, 2, 6, 3, 4, 5, 0, 0, 0, 0]