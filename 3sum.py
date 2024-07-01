def threeSum(nums):
    ans = set()
    nums.sort()
    for i in range (len(nums)):
        if i > 0 & nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                print(f"sum = {sum} nums[i] = {nums[i]}, nums[j] = {nums[j]}, nums[k] = {nums[k]}")
                ans.add((nums[i],nums[j],nums[k]))
                j += 1
                k -= 1
    return ans

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
nums = [0, 0, 0]
print(threeSum(nums))
nums = [0, 0, 0, 0]
print(threeSum(nums))
nums = [0,1,1]
print(threeSum(nums))
