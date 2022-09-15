def max_value(nums):
    max_value = -float("inf")
    for num in nums:
        if num > max_value:
            max_value = num
    return num