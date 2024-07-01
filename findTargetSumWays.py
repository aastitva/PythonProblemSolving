def fTSW_recurssion(nums, target, pos, curr_sum, memo):
    if (pos, curr_sum) in memo:
        return memo[(pos, curr_sum)]
    
    if pos == len(nums):
        return 1 if curr_sum == target else 0
    
    # Include current number with positive sign
    add = fTSW_recurssion(nums, target, pos+1, curr_sum + nums[pos], memo)
    # Include current number with negative sign
    subtract = fTSW_recurssion(nums, target, pos+1, curr_sum - nums[pos], memo)
    return add + subtract

def findTargetSumWays(nums, target):
    memo = {}
    return fTSW_recurssion(nums, target, 0, 0, memo)

# Example usage
nums = [11,31,37,36,43,40,50,18,10,15,10,35,43,25,41,43,6,22,38,38]
target = 44
print(findTargetSumWays(nums, target))

