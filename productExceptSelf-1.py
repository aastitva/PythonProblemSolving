def productExceptSelf(nums):
    prefix_mul = [1] * (len(nums))
    print(f"nums: {nums}")
    for L in range(len(nums)):
        prefix_mul[L] = nums[L] * prefix_mul[L-1] if L > 0 else nums[L]
    print(f"prefix_mul: {prefix_mul}")
    for R in range(len(nums)-1, -1, -1):
        if R == 0:
            prefix_mul[R] = multiplier
            break
        if R == len(nums) - 1:
            multiplier = 1
        prefix_mul[R] = prefix_mul[R-1] * multiplier
        multiplier = nums[R] * multiplier
        print(f"R: {R}, prefix_mul[R]: {prefix_mul[R]}, prefix_mul[R-1]: {prefix_mul[R-1]}, multiplier: {multiplier}")
        
    print(f"R: {R}, prefix_mul[R]: {prefix_mul[R]}, prefix_mul[R-1]: {prefix_mul[R-1]}, multiplier: {multiplier}")
    return prefix_mul

nums = [[1,2,4,6],[1,2,3,4],[0,0],[1,0],[-1,1,0,-3,3]]
for num in nums:
    print(productExceptSelf(num))