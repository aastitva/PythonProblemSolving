def subarraySum(nums,k):
    prefix_sum = {0:1}
    result = 0
    commulative_sum = 0
    for num in nums:
        commulative_sum += num
        diff = commulative_sum - k
        result += prefix_sum.get(diff,0)
        prefix_sum[commulative_sum] = 1 + prefix_sum.get(commulative_sum,0)

    return result

nums = [[1,-1,0]]
k = [0]
for i in range(len(nums)):
    print(subarraySum(nums[i], k[i]))