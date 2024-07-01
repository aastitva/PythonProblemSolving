def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev1 = 0
    prev2 = 0
    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr
    return prev1

nums = [[1,2,3,1],[2,7,9,3,1],[2,1,1,2],[2,3,2],[1,2],[1,2,1,1],[1,3,1],[2,1,1,2]]
for i in nums:
    print(f"\ni = {i}")
    print(f"rob = {rob(i)}")