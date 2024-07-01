def missingNumber(nums):
    sum = 0
    n = len(nums) + 1
    for i in nums:
        sum += i
    return (n * (n-1))//2 - sum


nums = [3,0,1]
print(missingNumber(nums))
nums = [0,1]
print(missingNumber(nums))
nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))