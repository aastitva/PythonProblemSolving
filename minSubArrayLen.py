def minSubArrayLen(target, nums):
    L = R = total = 0
    length = len(nums) + 1
    while R < len(nums):
        total += nums[R]
        while total >= target:
            length = min(length, R - L + 1)
            total -= nums[L]
            L += 1
        R += 1
        print(f" L: {L}, R: {R}, total: {total}, length: {length}")
    return 0 if length == len(nums) + 1 else length

nums = [[2,3,1,2,4,3],[1,4,4],[1,1,1,1,1,1,1,1],[1,2,3,4,5],[1,1,1,1,1,1,1,1],[1,2,3,4,5]]
target = [7,4,11,11,11,15]
for i in range(len(nums)):
    print(minSubArrayLen(target[i], nums[i]))

    