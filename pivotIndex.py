def pivotIndex(nums):
    L = 0
    R = len(nums) - 1
    prefix_sum = [0] * (R+1)
    for i in range(len(nums)):
        prefix_sum[i] = prefix_sum[i-1] + nums[i] if i > 0 else nums[i]
    for L in range(len(nums)):
        result = prefix_sum[R] - prefix_sum[L-1] if L > 0 else prefix_sum[R]
        if prefix_sum[L] == result:
            return L
        print(f"nums: {nums}, prefix_sum[R]: {prefix_sum[L-1]}, nums[L-1]: {nums[L-1]}, R: {R}, result: {result}")
    return -1

nums = [[1,7,3,6,5,6],[-1,-1,-1,0,1,1],[2,1,-1],[1,2,3],[1,1,1,1,1,1,1,1],[1,2,3,4,5]]
for i in range(len(nums)):
    print(pivotIndex(nums[i]))