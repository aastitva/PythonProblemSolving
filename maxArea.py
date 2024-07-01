def maxArea(nums):
    left = 0
    right = len(nums) - 1
    maxArea = 0
    while left < right:
        maxArea = max(maxArea, min(nums[left],nums[right]) * (right-left))
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return maxArea

nums = [1,8,6,2,5,4,8,3,7]
print(maxArea(nums))