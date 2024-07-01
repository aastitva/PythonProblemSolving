def maxSubArray(nums):
    curr_max = nums[0]
    overall_max = nums[0]
    for i in range(len(nums)):
        curr_max += nums[i]
        if curr_max <= nums[i]:
            curr_max = nums[i]
        overall_max = max(overall_max, curr_max)
    return overall_max

def maxSubArray2(nums):
    curr_max = 0
    overall_max = float('-inf')
    for num in nums:
        curr_max = max(num, curr_max + num)
        overall_max = max(overall_max, curr_max)
    return overall_max

def maxSubArray3(nums):
    sum = 0
    overall_max = float('-inf')
    for num in nums:
        sum = sum + num
        overall_max = max(overall_max, sum)
        if sum < 0 :
            sum = 0
    return overall_max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
print(maxSubArray2(nums))
print(maxSubArray3(nums))